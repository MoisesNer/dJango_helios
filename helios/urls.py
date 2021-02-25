from django.urls import path
from . import views

app_name = 'helios'

urlpatterns = [
    path('', views.home, name='homepage')
]