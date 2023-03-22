from django.urls import path

from recipes.views import home

from . import views

urlpatterns = [
    path('', home),
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
