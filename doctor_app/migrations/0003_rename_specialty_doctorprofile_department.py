# Generated by Django 4.2.11 on 2024-06-22 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0002_alter_doctorprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorprofile',
            old_name='specialty',
            new_name='department',
        ),
    ]
