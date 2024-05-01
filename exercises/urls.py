from django.urls import path

from exercises import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('part/<str:part>', views.choosed_part_modal, name="index" ),
    path('part/add-exercise/', views.add_exercise ),
    path('search/<str:query>', views.search_exercises, name="search" ),
    
    path('exercises/', views.exercises ,name="exercises")
    
    
]
