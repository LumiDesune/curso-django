from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return render(request, 'recipes/contact.html', context=None)


def users(request):
    usuario = {
        'nome': 'Lumi',
        'idade': 24,
        'profissao': 'Desenvolvedor Django'
    }

    return render(request, 'recipes/users.html', context={"usuario": usuario})


def user_list(request):
    usuarios = ['Lumi', 'Sant', 'Aurora', 'Jão', 'Crazy', 'Colvsk']

    return render(
        request,
        'recipes/list.html',
        context={'usuarios': usuarios}
    )

def sobre(request):
    return HttpResponse("Sobre o site")