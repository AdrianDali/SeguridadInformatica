# cifrado_app/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserRegistrationView,
    UserLoginView,
    CifradoCesarView,
    DescifradoCesarView,
    CifradoVigenereView,
    DescifradoVigenereView,
    CifradoPlayfairView,
    DescifradoPlayfairView,
)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cifrado/cesar/', CifradoCesarView.as_view(), name='cifrado_cesar'),
    path('descifrado/cesar/', DescifradoCesarView.as_view(), name='descifrado_cesar'),
    path('cifrado/vigenere/', CifradoVigenereView.as_view(), name='cifrado_vigenere'),
    path('descifrado/vigenere/', DescifradoVigenereView.as_view(), name='descifrado_vigenere'),
    
    path('cifrado/playfair/', CifradoPlayfairView.as_view(), name='cifrado_playfair'),
    path('descifrado/playfair/', DescifradoPlayfairView.as_view(), name='descifrado_playfair'),
]
