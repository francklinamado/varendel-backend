from django.urls import path
from .views import ApiRootView, GuardiansAPIView, GuardianAPIView, StudentsAPIView, StudentAPIView 

urlpatterns = [
    path ('', ApiRootView.as_view (), name ='api-root' ),
    path ('guardians/',GuardiansAPIView.as_view (),name='guardians' ),
    path ('guardians/<int:pk>',GuardianAPIView.as_view (), name = 'guardian'),
    path ('students/', StudentsAPIView.as_view (), name = 'students' ),
    path ('students/<int:pk>', StudentAPIView.as_view (), name= 'student')
]
