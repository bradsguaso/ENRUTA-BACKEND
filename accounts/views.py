from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def login(request):
    return Response({'Juan','Pedro'})

@api_view(['POST'])
def register(request):
    return Response({})

@api_view(['POST'])
def profile(request):
    return Response({})
