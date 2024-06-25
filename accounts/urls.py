from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.login_view, name='login'),

    path('registers/', views.register, name='registers'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard', views.base_page, name='patient_dashboard'),
]