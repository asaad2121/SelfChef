from django.urls import path, include
from food_app.views import index, food_det

urlpatterns= [ 
    path('', index , name = "index"),
    path('', index, name='search_results'),
    path('', index, name='show_recs'),
    path('<int:id>',food_det,name="food_det")
]