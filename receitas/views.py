from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics
from receitas.models import Receitas
from receitas.serializer import ReceitasSerializers

# Create your views here.

class ReceitasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializers

class ReceitasRetriveView(generics.RetrieveAPIView):
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializers

