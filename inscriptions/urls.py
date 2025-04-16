from django.urls import path,include
from .views import InscriptionViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter ()
router.register ('inscriptions', InscriptionViewSet)

urlpatterns = [
    path ("", include (router.urls))
]

