from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=1000000)
    prenom = models.CharField(max_length=1000000, default=None)
    numeros = models.IntegerField()
    email = models.EmailField( max_length=1000000)
    password = models.CharField(max_length=1000000)
    genre = models.CharField(max_length=1000000)

    def __str__(self):
        return self.email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = make_password(self.password, salt='pkwort')

class Homme(models.Model):
    nom_homme = models.CharField(max_length=1000000)
    description = models.CharField(max_length=1000000)
    photos = models.ImageField(height_field=None, width_field=None, max_length=None)
    nombre_article = models.IntegerField()
    prix = models.IntegerField()

    def __str__(self):
        return self.nom_homme


class Femme(models.Model):
    nom_femme = models.CharField(max_length=1000000)
    description = models.CharField(max_length=1000000)
    photos = models.ImageField(height_field=None, width_field=None, max_length=None)
    nombre_article = models.IntegerField()
    prix = models.IntegerField()

    def __str__(self):
        return self.nom_femme


class Enfant(models.Model):
    nom_enfant = models.CharField(max_length=1000000)
    description = models.CharField(max_length=1000000)
    photos = models.ImageField(height_field=None, width_field=None, max_length=None)
    nombre_article = models.IntegerField()
    prix = models.IntegerField()

    def __str__(self):
        return self.nom_enfant


class Chaussure(models.Model):
    nom_chaussure = models.CharField(max_length=1000000)
    description = models.CharField(max_length=1000000)
    photos = models.ImageField(height_field=None, width_field=None, max_length=None)
    nombre_article = models.IntegerField()
    prix = models.IntegerField()

    def __str__(self):
        return self.nom_chaussure