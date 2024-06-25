from .models import Patient,HealthResource,BillingStatement,Appointment,MedicalRecord
from django.contrib import admin
admin.site.register(Patient)


admin.site.register(HealthResource)
admin.site.register(MedicalRecord)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_and_time', 'status')

@admin.register(BillingStatement)
class BillingStatementAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount_due', 'due_date', 'payment_status')