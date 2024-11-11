from rest_framework import serializers
from .models import MedicalRecord
from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment


class MedicalRecordSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(read_only=True)
    appointment_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Appointment.objects.all(), source="appointment"
    )

    class Meta:
        model = MedicalRecord
        fields = "__all__"
