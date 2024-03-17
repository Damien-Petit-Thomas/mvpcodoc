# Utilisation de l'image python 3.9 comme base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

COPY requirements.txt /
RUN pip install -r /requirements.txt
# Génération des clés RSA avec mot de passe
COPY generate_keys.py /app
RUN python3 /app/generate_keys.py

# Copier le code source dans le conteneur
COPY app.py /app

# Installer les dépendances
# Commande pour exécuter l'application
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
