# cifrado_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CifradoPlayfairSerializer(serializers.Serializer):
    mensaje = serializers.CharField()
    clave = serializers.CharField()

# Serializador para crear un nuevo usuario
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, help_text='Requerido', style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializador para autenticar al usuario
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales inválidas")

# Serializadores para cifrado y descifrado
class CifradoCesarSerializer(serializers.Serializer):
    mensaje = serializers.CharField()
    desplazamiento = serializers.IntegerField()

class CifradoVigenereSerializer(serializers.Serializer):
    mensaje = serializers.CharField()
    clave = serializers.CharField()
    
class CifradoVernamSerializer(serializers.Serializer):
    mensaje = serializers.CharField()
    clave = serializers.CharField()

    def validate(self, data):
        mensaje = data.get('mensaje')
        clave = data.get('clave')
        if len(mensaje) != len(clave):
            raise serializers.ValidationError("La longitud del mensaje y la clave deben ser iguales.")
        return data
