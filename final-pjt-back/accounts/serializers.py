from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import MovieSerializer

class UserSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True, read_only=True)
 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'last_name', 'email', 'followings', 'like_movies')
        # fields = '__all__'
        read_only_fields = ('followings', 'like_movies')
