from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from xhtml2pdf import pisa

from .forms import TimeSheetCreateForm
from .models import TimeSheet


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        times = TimeSheet.objects.all().values()
        times_dict = {"times": times}
        pdf = render_to_pdf("overtime/timesheet_list.html", times_dict)
        return HttpResponse(pdf, content_type="application/pdf")


class TimeSheetListView(ListView):
    model = TimeSheet


class TimeSheetCreateView(CreateView):
    model = TimeSheet
    form_class = TimeSheetCreateForm
    
    def get_success_url(self):
        return reverse_lazy('overtime:overtime-list')


class TimeSheetDetailView(DetailView):
    model = TimeSheet
