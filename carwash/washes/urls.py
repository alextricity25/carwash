from django.urls import path

from . import views

urlpatterns = [
    path('', views.washes, name='washes'),
]
