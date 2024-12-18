from django.urls import path
from .views import UserRegistrationView, ChatView, UserLoginView, TokenBalanceView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('balance/', TokenBalanceView.as_view(), name='token-balance'),  # New Token Balance API endpoint
]
