from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from community.models import Review
from movies.models import Comment, Genre, Movie
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['POST'])
def signup(request):
    # 아이디, 비밀번호, 비밀번호 확인
    password = request.data.get('password')
    passwordConfirm = request.data.get('password1')
    if not password:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) ## 비밀번호 안쓰면 405
    # print(request.data)

    if password != passwordConfirm:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED) ## 비번 다르면 401

    serializer = UserSerializer(data=request.data)
    # print(serializer)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 hash 해서 저장
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    password = request.data.get('password')
    username = request.data.get('username')
    # print(password, username)
    users = User.objects.get(username = username) # 아이디 틀리면 500
    # print(users)
    # print(serializer)
    if check_password(password, users.password):
        print('통과함?')

        serializer = UserSerializer(users)
        token = TokenObtainPairSerializer.get_token(users)
        refresh_token = str(token)
        access_token = str(token.access_token)

        data = {
            "user": serializer.data,
            "message": "register success",
            "token":{
                "accessToken" : access_token,
                "refresh": refresh_token,
            },
        }
        return Response(data, status = 200)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST) # 비밀번호 틀리면 400 에러


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username = username)
    serializer = UserSerializer(user)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user

    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            is_followed = False
        else:
            person.followers.add(user)
            is_followed = True

        context = {
            'is_followed': is_followed,
            'followers_count': person.followers.count(),
            'followings_count': person.followings.count(),
        }
        # print(context)
        return Response(context)