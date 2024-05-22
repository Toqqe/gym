from django.urls import path

from exercises import views

urlpatterns = [
    path('', views.index, name="index" ),
    
    path('part/<str:part>', views.choosed_part_modal ),
    path('part/add-exercise/', views.add_exercise ),
    
    path('search/<str:query>', views.search_exercises, name="search" ),
    
    path('exercises/', views.exercises ,name="exercises"),
    
    path('exercise/edit/', views.edit_exercise),
    path('exercise/edit/<str:id>', views.get_exercise),
    path('exercise/delete/', views.delete_exercise)
]
