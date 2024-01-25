from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur
import os
from pathlib import Path

import csv

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

def export_to_csv(request):
    user = Utilisateur.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachement; filename = profile_export.csv'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Nom', 'Prenom', 'Email', 'Numeros', 'Password', 'Genre'])
    profile_fields = user.values_list('id', 'nom', 'prenom', 'email', 'numeros','password', 'genre' )

    for user in profile_fields:
        writer.writerow(user)
    return response

def import_csv(request):
    location = os.path.join(BASE_DIR)+'/profile_export(2).csv'
    f = open(r''+location)
    myReader = csv.reader(f)
    for row in myReader:
        print(row[4])
        photo = Utilisateur.objects.create(
                nom = row[1],
                prenom = row[2],
                numeros = int(row[4]),
                email = row[3],
                password = row[5],
                genre = row[6],
            )
        print(row[0], row[1], row[2], row[3])
        
    return location

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
