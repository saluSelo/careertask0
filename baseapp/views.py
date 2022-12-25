from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response

from baseapp.models import post
from baseapp.serializers import baseappSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def post_list(request):
        posts = post.objects.all()
        serializer = baseappSerializer(posts, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def add_post(request):
        serializer = baseappSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)