from django.urls import path
from .views import InscriptionViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter ()
router.register ('inscriptions', InscriptionViewSet)
