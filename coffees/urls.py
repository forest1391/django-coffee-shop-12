from django.urls import path

from . import views


app_name = 'coffees'
urlpatterns = [
    # ex: /coffees/
    path('', views.index, name='index'),

    path('<int:pk>/', views.show, name='show'),

    path('add/', views.add, name='add'),
]