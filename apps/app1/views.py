from django.shortcuts import render,redirect
from django.http import HttpResponse

from apps.app1.models import Contatos1
from apps.app1.models import Subestacoes
from .forms import SubestaoesForm
dados = Contatos1.objects.all()
#def index(requisicao):
    #return HttpResponse("<h1> ****Meu primeiro APP em Django****</h1>")

def index(requisicao):
    return render(requisicao,'index.html') #index.html

def arearestrita(requisicao):
    return render(requisicao,'area_restrita1.html')

def home(requisicao):
    return render(requisicao,'home.html',{"Contatos1":dados})

def cadastrar_subestacao(request):
    if request.method == 'POST':
        form = SubestaoesForm(request.POST)
        if form.is_valid():    
            form.save()
            return redirect('listar_produtos')
    else:
        form = SubestaoesForm()    
    return render(request,'Cadastro.html',{'form':form})

def listar_produtos(request):
    subestacoes1 = Subestacoes.objects.all()
    return render(request, 'lista_produtos.html', {'Subestacoes': subestacoes1})




# Create your views here.
