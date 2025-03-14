from django.contrib.staticfiles.views import serve
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer


# Create your views here.

@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

    token = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def profile(request):
    return Response({})


@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = CustomUser.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'Token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    return Response({"Deslogueado"})
