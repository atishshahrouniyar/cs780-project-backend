# urls.py
from django.urls import path, include
from .views import PatientRegistrationView, DoctorRegistrationView, OrganDonorView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("patient", PatientRegistrationView)
router.register("doctor", DoctorRegistrationView)
router.register("organ-donor", OrganDonorView)

urlpatterns = [
    path("", include(router.urls)),
]
