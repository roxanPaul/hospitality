from django.db import models
from django.contrib.auth.models import User




class DoctorProfile(models.Model):

    name=models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)



    def __str__(self):
        return self.name


class Appointment(models.Model):
    APPOINTMENT_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('rescheduled', 'Rescheduled'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey('patient_app.Patient', on_delete=models.CASCADE, related_name='doctor_patient_appointments')
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES)

    def __str__(self):
        return f"{self.patient.name} - {self.date_and_time}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey('patient_app.Patient', on_delete=models.CASCADE, related_name='medical_records')
    diagnoses = models.TextField()
    medications = models.TextField()
    treatment_plan = models.TextField()

    def __str__(self):
        return f"Medical record for {self.patient.name}"
