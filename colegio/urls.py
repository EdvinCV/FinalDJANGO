from django.urls import path
from . import views
from django.contrib.auth import views as vista

urlpatterns = [
    path('consulta/new', views.consulta_new, name="consulta_new"),
]