# Generated by Django 4.2.11 on 2024-06-22 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0004_doctorprofile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='user',
        ),
    ]
