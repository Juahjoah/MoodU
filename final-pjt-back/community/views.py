

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Review
from rest_framework.decorators import permission_classes

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        movies = get_list_or_404(Review)
        serializer = ReviewSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)