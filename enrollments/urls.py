from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import EnrollmentsViewSet

router = SimpleRouter ()
router.register ('enrollments',EnrollmentsViewSet)

urlpatterns = [
    path("", include (router.urls)),
]
