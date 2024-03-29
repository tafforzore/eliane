@@ -4,28 +4,20 @@ WORKDIR /
RUN python -m pip install --upgrade pip
RUN python -m pip install django
RUN python -m pip install virtualenv
RUN python -m pip install Pillow
RUN virtualenv env
RUN source/bin/activate
RUN ls
#COPY . /app/

# Exposez le port sur lequel votre application Django fonctionne (par défaut 8000)
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=eliane.settings
ENV DEBUG=False
WORKDIR /eliane
RUN ls
COPY . /eliane/
RUN mkdir -p eliane/staticfiles

RUN ls
RUN virtualenv env
RUN chmod +x env/bin/activate
RUN ls
RUN mkdir -p eliane/
# Collectez les fichiers statiques de Django
RUN python manage.py collectstatic --noinput
RUN mkdir -p staticfiles

# Appliquez les migrations de la base de données (si nécessaire)
RUN python manage.py makemigrations
#RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
#CMD ["python", "manage.py", " main()", "0.0.0.0:8000"]

# Commande pour exécuter votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
