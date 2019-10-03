from django.urls import path

from . import views

urlpatterns = [
    path('create-wash/', views.WashesCreate.as_view(), name='washes-create'),
    path('', views.WashesList.as_view()),
    path('<pk>/', views.WashesDetail.as_view(), name='washes-detail'),
]
