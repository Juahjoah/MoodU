from django.shortcuts import render
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

import requests
from .models import Movie, Comment, Genre
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer


# 장르 가져와서 저장하기
def get_movie_genre() :
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'language': 'ko-KR',
        'api_key': '***REMOVED***'
    }

    response = requests.get(url, params = params).json()
    
    for genre in response['genres']:
        if not Genre.objects.filter(name = genre['name']).exists():
            genre_data = Genre.objects.create(id = genre['id'], name = genre['name'])


# 영화 가져와서 저장하기
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
@permission_classes([IsAuthenticated])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    # print(request.user)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_movie(request, emotion): # happy, sad, soso, angry, joy, depressed

    if emotion == 'happy': # 판타지, 가족, 애니메이션, 스릴러, TV 영화 (except 공포, 스릴러, 범죄)
        accept_ids = [14, 10751, 16, 53, 10770]
        except_ids = [27, 53, 80]
        
    elif emotion == 'sad': # 애니메이션, 코미디, 모험, 음악, 가족 (except 전쟁, 로맨스, 범죄)
        accept_ids = [16, 35, 12, 10402, 10751]
        except_ids = [10752, 10749, 80]
        
    elif emotion == 'soso': # 공포, SF, 다큐멘터리, 역사, 음악 (except 전쟁, 로맨스)
        accept_ids = [27, 878, 99, 36, 10402]
        except_ids = [10752, 10749, 16]

    elif emotion == 'angry': # 액션, 모험, 애니메이션, 코미디 (except 범죄, 다큐멘터리, 로맨스)
        accept_ids = [28, 12, 16, 35, 878]
        except_ids = [80, 99, 10749]

    elif emotion == 'joy': # 모험, SF, 미스터리, 판타지, 음악 (except 공포, 전쟁, 로맨스)
        accept_ids = [12, 878, 9648, 14, 10402]
        except_ids = [10752, 27, 10749]

    elif emotion == 'depressed': # 코미디, 음악, 판타지, 드라마, 액션 (except 전쟁, 로맨스, 범죄)
        accept_ids = [35, 10402, 14, 18, 28]
        except_ids = [10752, 27, 10749]

    movies = Movie.objects.filter(genres__in = accept_ids)
    serializer = MovieSerializer(movies, many=True)

    # print(serializer.data)
    filtered_data = []
    for data in serializer.data:
        # print(data['genres'])
        gen = [gen['id'] for gen in data['genres']] # data안의 장르들을 for문으로 가져오고, 그들의 id를 list화
        print(gen)
        
        if all(g not in except_ids for g in gen): # gen의 g를 돌면서 g가 모두 except_ids에 포함되지 않으면
            filtered_data.append(data)

    return Response(filtered_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    
    if movie.like_users.filter(pk = user.pk).exists():
        movie.like_users.remove(user)
        is_liked = False
    else:
        movie.like_users.add(user)
        is_liked = True

    context = {
            'is_liked': is_liked,
            'liked_count': movie.like_users.count(),
        }

    return Response(context)

