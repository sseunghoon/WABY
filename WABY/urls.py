
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mlic/', include('mlic.urls')),
    path('admin/', admin.site.urls),
]
