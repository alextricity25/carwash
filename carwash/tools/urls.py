from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToolsList.as_view()),
]
