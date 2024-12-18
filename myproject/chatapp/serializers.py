from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # Create a new user and set tokens to 4000
        user = User.objects.create(**validated_data)
        user.tokens = 4000
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            if user.password == data['password']:
                return user
            raise serializers.ValidationError("Incorrect password")
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['user', 'message', 'response', 'timestamp']
