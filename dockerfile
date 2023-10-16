# Utilisation de l'image Python officielle comme base
FROM python:3.9

# Mettez en place le répertoire de travail
WORKDIR /eliane

# Mise à jour de pip et installation de Django, virtualenv et Pillow
RUN python -m pip install --upgrade pip
RUN python -m pip install django
RUN python -m pip install virtualenv
RUN python -m pip install Pillow

# Copiez le contenu de votre répertoire local dans le conteneur
COPY . /eliane/

# Créez le répertoire pour les fichiers statiques
RUN mkdir -p /eliane/staticfiles

# Créez et activez un environnement virtuel
RUN virtualenv env
RUN . /eliane/env/bin/activate

# Collectez les fichiers statiques de Django
RUN python manage.py collectstatic --noinput

# Appliquez les migrations de la base de données (si nécessaire)
RUN python manage.py makemigrations
RUN python manage.py migrate

# Exposez le port sur lequel votre application Django fonctionne (par défaut 8000)
EXPOSE 8000

# Définissez les variables d'environnement Django
ENV DJANGO_SETTINGS_MODULE=eliane.settings
ENV DEBUG=False

# Commande pour exécuter votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
