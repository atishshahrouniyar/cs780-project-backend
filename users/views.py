# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer
from rest_framework import viewsets

class PatientRegistrationView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DoctorRegistrationView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    