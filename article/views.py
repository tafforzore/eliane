from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def a_propos(request):
    return render(request, 'apropos.html')

def category(request):
    return render(request, 'category.html')

def error_404(request):
    return render(request, '404.html')

def login(request):
    return render(request, 'login.html')

def product_infos(request):
    return render(request, 'product_infos.html')