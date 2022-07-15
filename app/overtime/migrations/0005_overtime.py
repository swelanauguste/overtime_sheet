# Generated by Django 4.0.6 on 2022-07-08 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overtime', '0004_timesheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='overtime.employee')),
                ('time_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='overtime.timesheet')),
            ],
        ),
    ]
