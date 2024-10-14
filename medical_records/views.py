from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MedicalRecordSerializer
from .models import MedicalRecord


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
