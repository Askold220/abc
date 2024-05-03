from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_form, name='message_form'),
]
