from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('profile/<str:username>/', views.profile),
    path('<int:user_pk>/follow/', views.follow),
]