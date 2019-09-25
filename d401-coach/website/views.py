from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):

    if request.method == 'POST':
        data = Coach()
        data.nome = request.POST['nome']
        data.frase = request.POST['frase']
        data.inspirador = request.POST['inspirador']
        data.save()
        args = {
            'msg' : 'Voce foi cadastrado'
        }
        return render(request, 'index.html', args) 

    return render(request, 'index.html') 


def listar_coachs(request):
    listar_coachs = Coach.objects.all()
    print(listar_coachs)
    args = {
        'lista' : listar_coachs
    }
    return render(request, 'listar_coachs.html', args)

