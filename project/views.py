# AQUI VAI ESTAR ARMAZENADO AS VIEWS DAS PAGINAS
from django.http import HttpResponse

def sobre(request):
    return HttpResponse("Sobre do site")

def usuario(request, id):
    print(request.method)
    print(request.headers)

    return HttpResponse(f"Usuario: {id}")

def produtos(request):
    categoria = request.GET.get("categoria")

    return HttpResponse("Categoria: {}".format(categoria))