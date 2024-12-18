from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # To create a token

from . import views

urlpatterns=[
    path('auth/', obtain_auth_token),
    path('', views.api_home)
]
