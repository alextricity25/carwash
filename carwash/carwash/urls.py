from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('tools/', include('tools.urls')),
    path('washes/', include('washes.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'))
]
