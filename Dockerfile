FROM python:3.9

WORKDIR /
RUN python -m pip install --upgrade pip
RUN python -m pip install django

#COPY . /app/

# Exposez le port sur lequel votre application Django fonctionne (par défaut 8000)
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=eliane.settings
ENV DEBUG=False
RUN mkdir -p /eliane/staticfiles


CMD ["python", "manage.py", "collectstatic", "--noinput"]
CMD ["python", "manage.py", "collectstatic", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
