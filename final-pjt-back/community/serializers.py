from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    # print(username)

    def get_username(self, obj): # obj : get_username() 메소드의 인자로 전달되는 객체
        # 이 메소드는 ReviewSerializer 클래스 내에서 username 필드를 위한 직렬화 메소드로 사용된다.
        # obj 인자를 통해 직렬화 되는 Review 객체를 전달 받는다. 즉 obj는 Review 객체의 인스턴스를 나타낸다.
        return obj.user.username
    
    class Meta:
        model = Review
        # fields = ('id', 'title', 'content',)
        fields = '__all__'
        read_only_fields = ('user',)