from django.urls import path
from . import views

urlpatterns = [
    path('planos/', views.planos),
    path('pagamento/', views.pagamento),
]
