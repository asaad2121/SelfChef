from django.urls import path
from .views import Registration,Login,Logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',Registration.as_view(),name = 'register'),
    path('login/', Login.as_view(), name="login"), 
    path('logout', Logout.as_view(), name="logout"), 
]