from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.community_list),
    path('create/', views.community_create),
]