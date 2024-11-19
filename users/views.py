from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer, UserAuthSerializer, ConfirmationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmationCode


@api_view(['POST'])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({"error": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)


    user = User.objects.create_user(username=username, password=password, is_active=False)
    confirmation_code = ConfirmationCode(user=user)
    confirmation_code.generate_code()

    return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user is not None:
        if not user.is_active:
            return Response({"error": "Пользователь не подтвержден."}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(data={'error': 'User not valid!'},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def confirmation_view(request):
    serializer = ConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code')
    try:
        confirmation_code = ConfirmationCode.objects.get(code=code)
        if confirmation_code.is_code_expired():
            return Response({"detail": "Код подтверждения истек."}, status=status.HTTP_400_BAD_REQUEST)
        user = confirmation_code.user
        user.is_active = True
        user.save()
        confirmation_code.delete()
        return Response({"message": "Пользователь  подтвержден."}, status=status.HTTP_200_OK)
    except ConfirmationCode.DoesNotExist:
        return Response({"detail": "Неверный код подтверждения."}, status=status.HTTP_400_BAD_REQUEST)