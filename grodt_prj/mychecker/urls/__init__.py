from django.urls import path

from .. import views
from .mycheckermodel import urlpatterns_mycheckermodel

app_name = "mychecker"

urlpatterns = [
    path('', views.index, name="index"),
]

urlpatterns += urlpatterns_mycheckermodel
