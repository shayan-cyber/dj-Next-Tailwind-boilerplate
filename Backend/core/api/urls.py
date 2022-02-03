from django.urls import path
from rest_framework.authtoken import views as rf_views
from . import views


urlpatterns = [
    path('api-token-auth/', rf_views.obtain_auth_token),
    path('register/',views.register,name='register'),
    path('', views.home, name="home"),
]