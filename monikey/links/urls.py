from django.urls import path
from . import views

urlpatterns = [
    path('links/', views.links),
]
