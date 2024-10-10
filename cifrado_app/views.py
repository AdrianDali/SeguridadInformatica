# cifrado_app/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    CifradoCesarSerializer,
    CifradoVigenereSerializer,
    CifradoPlayfairSerializer,
)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .utils import (
    cifrado_cesar,
    cifrado_vigenere,
    descifrado_vigenere,
    cifrar_playfair,
    descifrar_playfair,
)
 

from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CifradoCesarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CifradoCesarSerializer(data=request.data)
        if serializer.is_valid():
            mensaje = serializer.validated_data['mensaje']
            desplazamiento = serializer.validated_data['desplazamiento']
            resultado = cifrado_cesar(mensaje, desplazamiento)
            return Response({'resultado': resultado})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DescifradoCesarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CifradoCesarSerializer(data=request.data)
        if serializer.is_valid():
            mensaje = serializer.validated_data['mensaje']
            desplazamiento = -serializer.validated_data['desplazamiento']
            resultado = cifrado_cesar(mensaje, desplazamiento)
            return Response({'resultado': resultado})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CifradoVigenereView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CifradoVigenereSerializer(data=request.data)
        if serializer.is_valid():
            mensaje = serializer.validated_data['mensaje']
            clave = serializer.validated_data['clave']
            resultado = cifrado_vigenere(mensaje, clave)
            return Response({'resultado': resultado})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DescifradoVigenereView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CifradoVigenereSerializer(data=request.data)
        if serializer.is_valid():
            mensaje = serializer.validated_data['mensaje']
            clave = serializer.validated_data['clave']
            resultado = descifrado_vigenere(mensaje, clave)
            return Response({'resultado': resultado})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
###########################################################################

class CifradoPlayfairView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CifradoPlayfairSerializer(data=request.data)
        if serializer.is_valid():
            mensaje = serializer.validated_data['mensaje']
            clave = serializer.validated_data['clave']
            resultado = cifrar_playfair(mensaje, clave)
            return Response({'resultado': resultado})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DescifradoPlayfairView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CifradoPlayfairSerializer(data=request.data)
        if serializer.is_valid():
            mensaje = serializer.validated_data['mensaje']
            clave = serializer.validated_data['clave']
            resultado = descifrar_playfair(mensaje, clave)
            return Response({'resultado': resultado})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
