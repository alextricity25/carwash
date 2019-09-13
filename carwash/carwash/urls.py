from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('washes/', include('washes.urls'), name = 'washes'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view() , name = 'login'),
    path('auth/', include('social_django.urls', namespace = 'social')),
]
