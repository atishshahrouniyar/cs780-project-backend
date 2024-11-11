from rest_framework import serializers
from .models import MedicalRecord
from appointments.serializers import AppointmentSerializer


class MedicalRecordSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = "__all__"
