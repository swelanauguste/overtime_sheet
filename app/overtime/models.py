from datetime import datetime, time

from django.db import models
from django.urls import reverse


class JobTitle(models.Model):
    job_title = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return self.job_title


class Department(models.Model):
    department = models.CharField(max_length=55, unique=True)

    def __str__(self) -> str:
        return self.department


class Employee(models.Model):
    employee = models.CharField(max_length=55, unique=True)
    job_title = models.ForeignKey(
        JobTitle, on_delete=models.CASCADE, blank=True, null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True
    )
    supervisor = models.ForeignKey(
        "Employee",
        related_name="supervisors",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    salary = models.PositiveSmallIntegerField(default=0)

    @property
    def get_hourly_rate(self):
        return f"{(((self.salary * 12) / 52) / 5) / 8:.2f}"

    def __str__(self) -> str:
        return self.employee


class Multiplier(models.Model):
    multiplier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.multiplier}"


class TimeSheet(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField()
    reason = models.TextField("reason for overtime")
    start_time = models.TimeField(default="16:30:00")
    end_time = models.TimeField(default="16:30:00")
    multiplier = models.ForeignKey(Multiplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    # def get_absolute_url(self):
    #     return reverse("overtime:overtime-detail", kwargs={"pk": self.pk})

    @property
    def time_diff(self):
        return (
            datetime.strptime(str(self.end_time), "%H:%M:%S")
            - datetime.strptime(str(self.start_time), "%H:%M:%S")
        ).seconds / 3600

    @property
    def get_overtime(self):
        overtime = (float(self.multiplier.multiplier) * float(self.time_diff)) * float(
            self.employee.get_hourly_rate
        )
        return f"{overtime:.2f}"

    def __str__(self):
        return f"{self.get_overtime} hours ({self.time_diff})"


# class Overtime(models.Model):
#     time_sheet = models.ForeignKey(TimeSheet, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.employee.employee}"
