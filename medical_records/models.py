from django.db import models
import uuid
from users.models import Patient


# Create your models here.
class MedicalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointment = models.ForeignKey(
        "appointments.Appointment", on_delete=models.CASCADE
    )
    diagnosis = models.TextField()
    prescription = models.TextField()
    patient = models.ForeignKey(
        Patient, related_name="medical_records", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
