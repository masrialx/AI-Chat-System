from django.urls import path
from .views import UserRegistrationView
from .views import ChatView
from .views import UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('chat/', ChatView.as_view(), name='chat'),
]
