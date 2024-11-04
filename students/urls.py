from django.urls import path
from .views import GuardianAPIView, StudentAPIView, ApiRootView

urlpatterns = [
    path ('', ApiRootView.as_view (), name ='api-root' ),
    path ('guardian/',GuardianAPIView.as_view (),name='guardian' ),
    path ('student/', StudentAPIView.as_view (), name = 'student' )
]
