from django.shortcuts import render

# Create your views here.
from django.html import JsonResponse

# Create your views here.

def receitas(request):
    if request.method == 'GET':
        tarefa = {'id': 1234, 'atividade': 'Receitas de bolos'}
        return JsonResponse(receitas)

