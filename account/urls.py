from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name="account-view"),
    
    path('training/<int:id>/', views.training_view, name="training")
]
