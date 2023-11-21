from django.contrib.auth.models import User
from rest_framework import serializers

from store_app.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'address']


class UserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(source='userinfo', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'user_info']
