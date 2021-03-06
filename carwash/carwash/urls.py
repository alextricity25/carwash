from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('tools/', include('tools.urls')),
    path('washes/', include('washes.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login')
    #path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
