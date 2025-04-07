from django.shortcuts import render
from django.http.response import JsonResponse
from .services import gemini_service

def index(request):
    return render(request, 'index.html')

def enviar_mensagem(request):
    pergunta = request.POST['pergunta']
    
    request = gemini_service.getResponse(pergunta)

    return JsonResponse({'msg': request})
