from aiohttp import request
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from api.serializers import SerializerMain
from rest_framework import viewsets
from api.models import State




class MainViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all().order_by('title')
    serializer_class = SerializerMain

class ApiNew(APIView):
    def post(self, request):
        print(request.GET)
        print(request.data)
        return HttpResponse('ok')
    
