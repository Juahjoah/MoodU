

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Review
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer
import jwt


@api_view(['GET'])
def community_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def community_create(request):
    print(request.headers['Authorization'])
    token = request.headers['Authorization'][7:]
    print('-0---------------')
    print(token)
    test = jwt.decode(token, "jwt", algorithms="HS256")
    print('---------------------')
    print(test)
    # jwt.decode
    serializer = ReviewSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)