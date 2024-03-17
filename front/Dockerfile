# Utilisation de l'image python 3.9 comme base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le code source dans le conteneur
COPY app.py /app 
COPY templates /app/templates
COPY requirements.txt /

# Installer les dépendances
RUN pip install -r /requirements.txt

# Exposer le port 80
EXPOSE 80

# Commande pour exécuter l'application avec Gunicorn
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:80", "app:app"]
