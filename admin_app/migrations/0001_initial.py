# Generated by Django 4.2.11 on 2024-06-21 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('resources', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.facilitymanagement')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_patient_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
