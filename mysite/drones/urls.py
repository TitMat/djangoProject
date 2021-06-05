from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'drones'
urlpatterns = [
    # ex: /drones/
    path('', views.index, name='index'),
    # ex: /drones/5/
    path('<int:drone_id>/', views.detail, name='detail'),
    path('<int:simulation_id>/preparesimu/', views.preparesimu, name='preparesimu'),
    path('<int:simulation_id>/simulate/', views.simulate, name='simulate'),
    path('<int:simulation_id>/results/', views.results, name='results'),
]