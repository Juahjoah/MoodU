from django.shortcuts import render
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view

from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer

@api_view(['GET'])
def index(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)