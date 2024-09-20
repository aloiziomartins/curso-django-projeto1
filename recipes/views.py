from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'recipes/home.html', status=200, context={
        'name' : 'Aloizio Martins'

    })


#def home(request):
#    return HttpResponse("Página inicial recipes")

def contato(request):
    return HttpResponse("Contato recipes ")

def sobre(request):
    return HttpResponse("Sempre acredite em você! recipes")