
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.Patient_profile, name='profile'),
    path('contact/',views.contact,name='contact'),
    path('appointment_booking/', views.appointment_booking, name='appointment_booking'),
    path('billing_list/', views.view_billing, name='billing_list'),
    path('health-resources/', views.health_resources, name='health_resources'),
    path('',views.home,name='base'),
    path('complete_appointment/<int:id>',views.complete_appointment,name="complete_appointment"),
    path('facility_page/',views.facility_page,name='facility_page'),
    path('about/',views.about,name='about'),
    path('create_billing_session/<int:id>/',views.create_billing_session, name='create_billing_session'),
    path('display_profile/<str:username>/',views.display_profile,name='display_profile'),
    path('search/', views.search_view, name='search'),

]
