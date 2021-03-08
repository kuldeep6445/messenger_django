
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_login),
    path('chatview/',views.chatview),
]