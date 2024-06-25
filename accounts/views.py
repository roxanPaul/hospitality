from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib import auth

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Assign the user to a group based on role
            if user.role == 'patient':
                user.groups.add(Group.objects.get(name='Patients'))
            elif user.role == 'doctor':
                user.groups.add(Group.objects.get(name='Doctors'))
            elif user.role == 'admin':
                user.groups.add(Group.objects.get(name='Admins'))

            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user role
                if role == 'admin':
                    return redirect('admin_dashboard')
                elif role == 'doctor':
                    return redirect('doctor_dashboard')
                elif role == 'patient':
                    return redirect('base')
                else:
                    messages.error(request, 'Invalid role selected.')
            else:
                # Invalid login
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Form data is not valid.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})
@login_required
def admin_dashboard(request):
    return render(request, 'admin/home.html')
@login_required
def doctor_dashboard(request):
    return render(request, 'doctor/home.html')

@login_required
def base_page(request):
    return render(request, 'patient/home.html')