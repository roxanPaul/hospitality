from django.db import models
from django.contrib.auth.models import User
from patient_app.models import Patient
from doctor_app.models import DoctorProfile

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class FacilityManagement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    APPOINTMENT_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('rescheduled', 'Rescheduled'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='admin_doctor_appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='admin_patient_appointments')
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES)

    def __str__(self):
        return f"{self.patient.name} - {self.date_and_time}"

class AdminProfile(models.Model):
    role=models.CharField(max_length=20)
    permission=models.CharField(max_length=50)


