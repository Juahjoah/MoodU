from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/comments/create/', views.create_comment),
    path('<int:movie_pk>/comments/', views.comment),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comments_del_up),
    path('recommended/<str:emotion>/', views.recommend_movie),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/like/count/', views.like_movie_count),
    path('search/<str:movie_title>/', views.movie_search),
]