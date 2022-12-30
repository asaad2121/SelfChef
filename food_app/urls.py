from django.urls import path, include
from food_app import views

urlpatterns= [ 
    path('', views.index , name = "index"),
]