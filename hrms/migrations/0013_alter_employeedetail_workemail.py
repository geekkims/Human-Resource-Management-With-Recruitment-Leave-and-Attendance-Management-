# Generated by Django 4.0.5 on 2022-06-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0012_alter_employeedetail_workemail_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='workemail',
            field=models.EmailField(max_length=125),
        ),
    ]
