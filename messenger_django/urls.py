from django.contrib import admin
from django.urls import path,include
from Chatroom.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Chatroom.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('sign_up/', signup_view),
]