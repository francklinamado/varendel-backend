from django.contrib import admin
from django.urls import path, include
from students.urls import router
from inscriptions.urls import router

urlpatterns = [

    path('admin/', admin.site.urls),
    path ('auth/',include ('rest_framework.urls')),
    path ('api/v1/', include('students.urls')),
    path ('api/v2/', include (router.urls)),
    path ('', include('students.urls')),

]
