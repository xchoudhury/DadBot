from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

@api_view(['GET'])
def get_message(request):
    return Response(request.data)