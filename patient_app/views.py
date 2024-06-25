from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MedicalRecord, Appointment, BillingStatement, HealthResource,Patient,FacilityManagement
from .forms import PatientRegistrationForm, MedicalRecordForm, AppointmentForm,SearchForm
import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
import stripe

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def facility_page(request):
    facilities = FacilityManagement.objects.all()
    return render(request, 'patient/facility_page.html', {'facilities': facilities})
def Patient_profile(request):
    try:
        patient_profile = Patient.objects.get(id=request.user.id)  # Assuming you have some unique identifier like id
    except Patient.DoesNotExist:
        patient_profile = None

    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, instance=patient_profile)
        if form.is_valid():
            patient_profile = form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('appointment_booking')  # Replace 'base' with your actual redirect URL
    else:
        form = PatientRegistrationForm(instance=patient_profile)

    context = {
        'form': form,
    }
    return render(request, 'patient/profile.html', context)

@login_required
def display_profile(request):
    patient_profile = get_object_or_404(Patient, user=request.user)
    medical_records = MedicalRecord.objects.filter(patient=request.user)

    context = {
        'patient_profile': patient_profile,
        'medical_records': medical_records
    }
    return render(request, 'patient/display_profile.html', context)


def search_view(request):
    form = SearchForm(request.POST or None)
    results = None
    if request.method == 'POST' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = Patient.objects.filter(user__username__icontains=query)
    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'patient/search_results.html', context)
@login_required
def appointment_booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointment_booking')
    else:
        form = AppointmentForm()
    return render(request, 'patient/appointment_booking.html', {'form': form})

@login_required
def complete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 'completed'
    appointment.save()

    # Create or update the billing statement
    billing, created = BillingStatement.objects.get_or_create(appointment=appointment)
    if created:
        billing.amount_due = 100.00  # Set the appropriate amount
        billing.due_date = timezone.now() + timezone.timedelta(days=30)
        billing.save()

    return redirect('view_billing', billing_id=billing.id)

def success(request):
    return render(request, 'patient/success.html')
def cancel(request):
    return render(request,'patient/cancel.html')
@login_required
def health_resources(request):
    resources = HealthResource.objects.all()
    return render(request, 'patient/health_resources.html', {'resources':resources})


@login_required
def view_billing(request, billing_id):
    billing = get_object_or_404(BillingStatement, id=billing_id)
    return render(request, 'patient/billing_list.html', {'billing': billing})

def create_billing_session(request, id):
    try:
        bill = BillingStatement.objects.get(id=id)
    except BillingStatement.DoesNotExist:
        return redirect('billing')  # Redirect to billing page or handle error

    # Calculate amount due based on the appointment
    appointment = bill.appointment
    amount_due = appointment.cost

    # Create a line item for the Stripe Checkout session
    line_item = {
        'price_data': {
            'currency': 'INR',  # Adjust currency as per your requirement
            'unit_amount': int(amount_due * 100),  # Stripe uses the smallest currency unit
            'product_data': {
                'name': f'Billing Statement #{bill.id}',
            },
        },
        'quantity': 1,
    }

    # Create a Stripe Checkout session
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[line_item],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')),  # Adjust success and cancel URLs
        cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
    )

    return redirect(checkout_session.url, code=303)

def medical_record_display(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record saved successfully.')
            return redirect('medical_record_display')
    else:
        form = MedicalRecordForm()

    records = MedicalRecord.objects.all()

    context = {
        'form': form,
        'records': records,
    }
    return render(request, 'patient/medical_record_display.html', context)