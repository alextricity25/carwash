from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('washes/', include('washes.urls')),
    path('admin/', admin.site.urls),
]
