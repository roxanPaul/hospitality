# Generated by Django 4.2.11 on 2024-06-22 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
