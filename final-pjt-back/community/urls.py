from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.community_list),
    path('create/', views.community_create),
    path('<int:review_pk>/', views.community_detail),
    path('<int:review_pk>/update/', views.community_update)
]