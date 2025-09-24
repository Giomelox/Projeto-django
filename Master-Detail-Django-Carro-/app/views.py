from django.shortcuts import render, get_object_or_404
from .models import Produto

def home(request):
    return render(request, 'index_principal.html')

def produtos_tecnologia(request):
    produtos = Produto.objects.filter(categoria='tecnologia')
    return render(request, 'index.html', {'produtos': produtos})

def produtos_vestuario(request):
    produtos = Produto.objects.filter(categoria='vestuario')
    return render(request, 'index.html', {'produtos': produtos})

def detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes.html', {'produto': produto})