from django.shortcuts import render
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes

import requests
from .models import Movie, Comment, Genre
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer

def get_movie_genre() :

    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'language': 'ko-KR',
        'api_key': '***REMOVED***'
    }

    response = requests.get(url, params = params).json()
    
    for genre in response['genres']:
        if not Genre.objects.filter(name = genre['name']).exists():
            genre_data = Genre.objects.create(name = genre['name'])




# 데이터를 요청을 보내서 저장한다.
def get_movie_data() :
    for i in range(1, 4):
        URL = 'https://api.themoviedb.org/3/movie/popular'
        params = {
            'language':'ko-KR',
            'page': i,
            'api_key': '***REMOVED***'
        }

        movies = requests.get(URL, params=params).json()

        for movie in movies['results']:
            if not Movie.objects.filter(title = movie['title']).exists():
                print(movie)
                movie_data = Movie.objects.create(
                    title = movie['title'],
                    overview = movie['overview'],
                    release_date = movie['release_date'],
                    popularity = movie['popularity'],
                    vote_count = movie['vote_count'],
                    vote_average = movie['vote_average'],
                    poster_path = movie['poster_path'],
                )
                genre_ids = movie['genre_ids']
                genres = Genre.objects.filter(id__in = genre_ids)
                print(genres)
                movie_data.genres.set(genres)

                movie_data.save()



@api_view(['GET'])
def index(request):
    get_movie_genre()
    get_movie_data()
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])

def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    # print(request.user)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)