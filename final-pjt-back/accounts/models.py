from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    # follow기능에 필요한 M:N 중개모델, 정참조 : followings / 역참조 : followers
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')