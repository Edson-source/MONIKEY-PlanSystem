from django.urls import path
from .views import *

urlpatterns = [
    path('links/', links),
    path('<str:username>/admin/', admin_profile_view, name="username"),
]
