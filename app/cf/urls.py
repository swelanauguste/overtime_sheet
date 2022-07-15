from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("overtime/", include("overtime.urls", namespace="overtime")),
    path("admin/", admin.site.urls),
]
