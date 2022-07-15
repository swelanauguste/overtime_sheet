from django.contrib import admin
from .models import Employee, Department, JobTitle, Multiplier, TimeSheet

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(JobTitle)
admin.site.register(Multiplier)
admin.site.register(TimeSheet)
# admin.site.register(Overtime)