from rest_framework import routers
from .views import AppointmentViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("appointment", AppointmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
