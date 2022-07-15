from django import forms

from .models import TimeSheet


class TimeSheetCreateForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.DateInput(attrs={"type": "time"}),
            "end_time": forms.DateInput(attrs={"type": "time"}),
            "multiplier": forms.RadioSelect(),
            "reason": forms.Textarea(attrs={"rows": 4}),
        }
