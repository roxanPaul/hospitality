# Generated by Django 4.2.11 on 2024-06-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0003_rename_specialty_doctorprofile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='name',
            field=models.CharField(default=1234, max_length=20),
            preserve_default=False,
        ),
    ]
