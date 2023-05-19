from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from .serializers import UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

@api_view(['POST'])
def signup(request):
    # 아이디, 비밀번호, 비밀번호 확인
    password = request.data.get('password')
    passwordConfirm = request.data.get('passwordConfirm')
    # print(request.data)
    if password != passwordConfirm:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

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
    users = get_object_or_404(User, username = username)
    serializer = UserSerializer(users)
    # print(serializer.data)

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