from django.db import models
import uuid


# Create your models here.
class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey("users.Patient", on_delete=models.CASCADE, null=True)
    doctor_id = models.ForeignKey("users.Doctor", on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
