from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Movie, Comment, Genre
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer
    
import requests
import random


# 장르 api를 이용해 종류를 가져와 db에 저장
def get_movie_genre() :
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'language': 'ko-KR',
        'api_key': '6db32cec1c1344cc39fed57c1e290ab4'
    }

    response = requests.get(url, params = params).json()
    
    for genre in response['genres']:
        if not Genre.objects.filter(name = genre['name']).exists():
            genre_data = Genre.objects.create(id = genre['id'], name = genre['name'])


# 영화 api를 이용해 영화 list를 가져와 db에 저장
def get_movie_data() :
    for i in range(1, 5):
        URL = 'https://api.themoviedb.org/3/movie/popular'
        params = {
            'language':'ko-KR',
            'page': i,
            'api_key': '6db32cec1c1344cc39fed57c1e290ab4'
        }

        movies = requests.get(URL, params=params).json()

        for movie in movies['results']:
            if 'release_date' not in movie:
                continue
            
            if not Movie.objects.filter(title = movie['title']).exists() and not Movie.objects.filter(poster_path=movie['poster_path']).exists():
                    # print(movie)
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
                # print(genres)
                movie_data.genres.set(genres)

                movie_data.save()


# 전체 영화 list 전송
@api_view(['GET'])
def index(request):
    get_movie_genre()
    get_movie_data()
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 상세 영화 정보 전송
@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 영화에 따른 댓글 list 전송
@api_view(['GET'])
def comment(reqeust, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = Comment.objects.filter(movie = movie)
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)


# 특정 영화에 댓글 생성하고 db에 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    # print(request.user)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comments_del_up(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk, movie=movie)

    if request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response({'delete':f'{comment_pk}번 글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'user가 같지 않아 삭제할 수 없습니다.'})
    
    elif request.method == 'PUT':
        print(request.user, comment.user)
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)



    


# 영화 추천 알고리즘
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_movie(request, emotion): # happy, sad, soso, angry, joy, depressed
    # print(emotion)
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
        # print(gen)
        
        if all(g not in except_ids for g in gen): # gen의 g를 돌면서 g가 모두 except_ids에 포함되지 않으면
            filtered_data.append(data)

    ran_filtered_data = random.sample(filtered_data, 10)
    return Response(ran_filtered_data)


# 영화에 좋아요 개수 count
@api_view(['GET'])
def like_movie_count(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'like_count' : movie.like_users.count()
    }
    return Response(context)


# 좋아요를 눌렀을 때 추가하고 해제했을 때 삭제
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
        }
    return Response(context)

