from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index),
    path('<int:movie_pk>/', views.detail),
    # path('<int:movie_pk>/comments/create/', views.create_comment)
]