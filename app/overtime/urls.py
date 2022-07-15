from django.urls import path

from . import views

app_name = "overtime"

urlpatterns = [
    path("", views.TimeSheetListView.as_view(), name="overtime-list"),
    path(
        "detail/<int:pk>/", views.TimeSheetDetailView.as_view(), name="overtime-detail"
    ),
    path("create/", views.TimeSheetCreateView.as_view(), name="overtime-create"),
    path("pdf", views.ViewPDF.as_view(), name="pdf"),
]
