from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Changed related_name to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Changed related_name to avoid conflict
        blank=True,
    )


class Patient(User):
    blood_type = models.CharField(max_length=255)


class Doctor(User):
    specialization = models.CharField(max_length=255)


class OrganDonor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    donor = models.ForeignKey(
        Patient, related_name="organs_donated", on_delete=models.CASCADE
    )
    organ = models.CharField(max_length=255)
    availability_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
