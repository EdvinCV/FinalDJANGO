from django.urls import path
from . import views
from django.contrib.auth import views as vista

urlpatterns = [
    path('grado/new', views.asignacion_new, name="asignacion_new"),
]