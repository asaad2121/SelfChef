from django.urls import path, include
from food_app import views

urlpatterns= [ 
    path('', views.index , name = "index"),
    path('', views.index, name='search_results'),
    path('', views.index, name='show_recs'),
    path('<int:id>',views.food_det,name="food_det"),
    path('recepies', views.recepie_page, name="recepie_page"),
    path('recepies', views.recepie_page, name="search_recepie_page"),
    path('add_recepie', views.add_recepie, name="add_recepie"),
    path('edit_recepie/<int:id>/', views.edit_recepie, name="edit_recepie"),
    path('delete_recepie/<int:id>/', views.delete_recepie, name="delete_recepie"),
    
]