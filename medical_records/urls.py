from rest_framework import routers
from .views import MedicalRecordViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("medical-record", MedicalRecordViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
