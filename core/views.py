from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    #usuario = request.user
    #evento = Evento.objects.get(id=1)
    evento = Evento.objects.all()
    #evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
