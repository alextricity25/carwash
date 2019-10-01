from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tools/', include('tools.urls')),
    path('washes/', include('washes.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
