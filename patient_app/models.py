
from django.db import models
from django.contrib.auth.models import User
from doctor_app.models import DoctorProfile

class Patient(models.Model):

    name=models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name


class Appointment(models.Model):
    APPOINTMENT_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('rescheduled', 'Rescheduled'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='patient_doctor_appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES)





class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_medical_records')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctors_record')
    diagnoses = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()


    def __str__(self):
        return self.patient.name + "'s Medical Record"

class BillingStatement(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='billing_statements')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Billing Statement for {self.appointment.patient.name}"

class HealthResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)


    def __str__(self):
        return self.title



class FacilityManagement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=15)

    def __str__(self):
        return self.name