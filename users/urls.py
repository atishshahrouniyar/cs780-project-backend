# urls.py
from django.urls import path
from .views import PatientRegistrationView, DoctorRegistrationView

urlpatterns = [
    path('register/patient/', PatientRegistrationView.as_view(), name='register_patient'),
    path('register/doctor/', DoctorRegistrationView.as_view(), name='register_doctor'),
]
