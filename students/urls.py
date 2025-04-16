from django.urls import path, include
from .views import ApiRootView, GuardiansAPIView, GuardianAPIView, StudentsAPIView, StudentAPIView, StudentViewSet, GuardianViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter ()
router.register ('students', StudentViewSet)
router.register ('guardians', GuardianViewSet)
urlpatterns = [
      path("", include(router.urls)),
    #path ('guardians/',GuardiansAPIView.as_view (),name='guardians' ),
    #path ('guardians/<int:pk>/',GuardianAPIView.as_view (), name = 'guardian'),
    #path ('guardians/<int:pk>/students/',StudentsAPIView.as_view (), name= 'guardian_student'),
    #path ('students/', StudentsAPIView.as_view (), name = 'students' ),
    #path ('students/<int:pk>/', StudentAPIView.as_view (), name= 'student'),
    #path ('students/<int:pk>/guardians', GuardianAPIView.as_view (), name = "student_guardian"),
]
