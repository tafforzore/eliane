from django.contrib import admin
from article.models import Utilisateur, Homme, Femme, Chaussure, Enfant

# Register your models here.

@admin.register(Utilisateur)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','nom','prenom','numeros','email','password', 'genre')

@admin.register(Homme)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','nom_homme','description','photos','nombre_article','prix')

@admin.register(Femme)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','nom_femme','description','photos','nombre_article','prix')

@admin.register(Chaussure)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','nom_chaussure','description','photos','nombre_article','prix')

@admin.register(Enfant)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','nom_enfant','description','photos','nombre_article','prix')    
