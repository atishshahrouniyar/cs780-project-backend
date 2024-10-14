# urls.py
from django.urls import path, include
from .views import PatientRegistrationView, DoctorRegistrationView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patient', PatientRegistrationView)
router.register('doctor', DoctorRegistrationView)

urlpatterns = [
    path('', include(router.urls)),
]
