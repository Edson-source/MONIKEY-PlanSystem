from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>', user_view, name="user"),
    path('<str:username>', profile_view, name="username"),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user"),
    path('register/', register_user, name="register_user"),
    path('change_password/', change_password, name='change_password'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]