from rest_framework import serializers
from .models import Ad
from django.contrib.auth.models import User


#для каждого ада создаем сериализатор
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'ad_id', 'title', 'author', 'views', 'position']

#для пользователя создаем сериализатор
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    #для создания юзера
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user