FROM python:3.9

WORKDIR /
RUN python -m pip install --upgrade pip
RUN python -m pip install django

#COPY . /app/

# Exposez le port sur lequel votre application Django fonctionne (par défaut 8000)
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=eliane.settings
ENV DEBUG=False
RUN mkdir -p /eline/staticfiles
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Commande pour exécuter votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
