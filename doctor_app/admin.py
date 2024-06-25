from .models import DoctorProfile, Appointment,MedicalRecord
from django.contrib import admin
admin.site.register(DoctorProfile)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)