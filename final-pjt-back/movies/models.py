from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    # ids = models.IntegerField()
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    # movie와 genres M:N table
    genres = models.ManyToManyField(Genre)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies')


class Comment(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)