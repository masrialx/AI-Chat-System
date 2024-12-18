from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from .models import User, Chat
from .serializers import ChatSerializer
from django.utils import timezone
from .serializers import LoginSerializer
import random
import string
from django.core.exceptions import ObjectDoesNotExist

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # Generate a random token for authentication
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            return Response({"token": token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')

        if not token:
            return Response({"error": "Authentication token required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = User.objects.get(username="john_doe")  # In a real system, validate the token properly
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user.tokens < 100:
            return Response({"error": "Insufficient tokens."}, status=status.HTTP_400_BAD_REQUEST)

        user.tokens -= 100
        user.save()

        chat = Chat.objects.create(user=user, message=request.data['message'], response="AI response")

        # Serialize the chat response
        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenBalanceView(APIView):
    def get(self, request):
        # Get the token from the Authorization header
        token = request.headers.get('Authorization')

        if not token:
            return Response({"error": "Authentication token required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # In a real system, you would validate the token here properly, for example using JWT or another method
            user = User.objects.get(username="john_doe")  # Example user, replace with token validation logic
        except ObjectDoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"tokens": user.tokens}, status=status.HTTP_200_OK)
