

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
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_create(request):
    serializer = ReviewSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE'])
def community_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response({'delete':f'{review_pk}번 글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    


@api_view(['PUT'])
def community_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)