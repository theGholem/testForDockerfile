# Utiliser la version exacte de Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier Python dans le répertoire de travail du conteneur
COPY get_number.py .

# Exécuter le programme Python lors du démarrage du conteneur
CMD ["python", "get_number.py"]
