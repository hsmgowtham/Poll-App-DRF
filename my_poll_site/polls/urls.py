from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register("home", views.DashboardAPIView, basename="home")

urlpatterns = router.urls