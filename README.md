# Quote Generator

Projet d'apprentissage Docker composé d'une API Fast et d'une WebApp Flask
Contient les fichiers Dockerfile pour créer les 2 images
Contient le fichier docker-compose.yaml pour éxecuter les 2 container dans un bridge isolé

## Architecture
* **API** : Python 3.14 (Alpine), port 8000
    / : donne une quote aléatoirement
    /howmany : donne le nombre de quotes
* **WebAPP** : Python 3.14 (Alpine), port 5000

## Installation avec Docker

### 1. Constuire l'image API
```bash
cd api
docker build . -t quote_api

### 2. Construire l'image WebAPP
```bash
cd webapp
docker build . -t quote_webapp

### 3. Lancer les containeur 
```bash
docker compose up -d

### 4. Accès aux services
* ***API*** : http://<dockerhost>:8000
* ***WebApp*** : http://<dockerhost>:5000