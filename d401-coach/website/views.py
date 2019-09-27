from django.shortcuts import render, redirect 
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
    listar_coachs = Coach.objects.filter(ativo = True).all()
    args = None
    if listar_coachs.first() is None:
        args = {
            'msg' : 'nao tem ninguem aqui'
        }
    else:     
        args = {
            'lista' : listar_coachs
        }

    return render(request, 'listar_coachs.html', args)
    # return render(request, 'listar_coachs.html', msg)
        

def delete_coach(request, id):
    item = Coach.objects.filter(id=id).first()
    if item is not None:
        item.ativo = False
        item.save()

        listar_coachs = Coach.objects.filter(ativo=True).all()
        args = {
            'listar_coachs' : listar_coachs,
            'msg' : 'Deletado com sucesso.'
        }

        return redirect('/coachs/listar')
    return redirect('/')
