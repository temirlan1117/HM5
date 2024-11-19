from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmationCode


class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Username already exists')

class ConfirmationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    def validate_code(self, value):
        try:
            ConfirmationCode.objects.get(code=value)
        except ConfirmationCode.DoesNotExist:
            raise ValidationError('Неверный код')
        return value