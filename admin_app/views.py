from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import  DoctorProfileForm, PatientProfileForm,AppointmentManagementForm,FacilityForm
from django.apps import apps
from . models import FacilityManagement,Appointment
from django.contrib.auth import authenticate, login
from doctor_app.models import Appointment as DoctorAppointment
from patient_app.models import Appointment as PatientAppointment
from admin_app.models import Appointment as AdminAppointment

from .models import Patient, DoctorProfile, AdminProfile

from doctor_app.models import DoctorProfile




def home(request):
    return render(request,'admin/home.html')
def doctor_profile_update(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('list_doctor')  # Replace with your URL name for doctor profile list
    else:
        form = DoctorProfileForm(instance=doctor)
    return render(request, 'admin/update_doctor_profile.html', {'form': form})

def doctor_profile_delete(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctor')  # Replace with your URL name for doctor profile list
    return render(request, 'admin/delete_doctor_profile.html', {'doctor': doctor})


def doctor_profile_list(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'admin/list_doctor_profile.html', {'doctors': doctors})


def doctor_profile_add(request):
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_doctor')
    else:
        form = DoctorProfileForm()

    return render(request, 'admin/add_doctor_profile.html', {'form': form})



def add_patient(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_patient')  # Redirect to doctor profiles or any desired page
    else:
        form = PatientProfileForm()
    return render(request, 'admin/add_patient.html', {'form': form})

def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('list_patient')  # Redirect to doctor profiles or any desired page
    else:
        form = PatientProfileForm(instance=patient)
    return render(request, 'admin/update_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('list_patient')  # Redirect to doctor profiles or any desired page
    return render(request, 'admin/delete_patient.html', {'patient': patient})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'admin/patient_list.html', {'patients': patients})

def facility_list(request):
    facilities = FacilityManagement.objects.all()
    return render(request, 'admin/facility_list.html', {'facilities': facilities})


def facility_detail(request, pk):
    facility = get_object_or_404(FacilityManagement, pk=pk)
    return render(request, 'admin/facility_detail.html', {'facility': facility})


def facility_create(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility created successfully.')
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'admin/facility_add.html', {'form': form})


def facility_update(request, pk):
    facility = get_object_or_404(FacilityManagement, pk=pk)
    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility updated successfully.')
            return redirect('facility_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'admin/facility_update.html', {'form': form})


def facility_delete(request, pk):
    facility = get_object_or_404(FacilityManagement, pk=pk)
    if request.method == 'POST':
        facility.delete()
        messages.success(request, 'Facility deleted successfully.')
        return redirect('facility_list')
    return render(request, 'admin/facility_confirm_delete.html', {'facility': facility})


def appointment_list(request):
    doctor_appointments = DoctorAppointment.objects.all()
    admin_appointments = AdminAppointment.objects.all()
    patient_appointments = PatientAppointment.objects.all()
    # Combine all three querysets
    appointments = list(doctor_appointments) + list(patient_appointments) + list(admin_appointments)

    return render(request, 'admin/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'admin/appointment_detail.html', {'appointment': appointment})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentManagementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointment_list')
    else:
        form = AppointmentManagementForm()
    return render(request, 'admin/appointment_create.html', {'form': form})


def appointment_update(request, pk):
    Appointment = apps.get_model('doctor_app', 'Appointment')
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentManagementForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('appointment_list')
    else:
        form = AppointmentManagementForm(instance=appointment)

    return render(request, 'admin/appointment_form.html', {'form': form})
def appointment_delete(request, pk):
    Appointment = apps.get_model('doctor_app', 'Appointment')
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('appointment_list')
    return render(request, 'admin/appointment_confirm_delete.html', {'appointment': appointment})