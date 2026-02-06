# Quote Generator

Projet d'apprentissage Docker composé d'une API Fast et d'une WebApp Flask. 

Contient les fichiers Dockerfile pour créer les 2 images. 

Contient le fichier docker-compose.yaml pour éxecuter les 2 container dans un bridge isolé. 

## Architecture
* **API** : Python 3.14 (Alpine), port 8000. 

 / : donne une quote aléatoirement. 

 /howmany : donne le nombre de quotes. 

* **WebAPP** : Python 3.14 (Alpine), port 5000. 

## Installation avec Docker

```bash
### 1. Constuire l'image API
cd api
docker build . -t quote_api

### 2. Construire l'image WebAPP
cd webapp
docker build . -t quote_webapp

### 3. Lancer les containers 
docker compose up -d
````

## Accès aux services
* **API** : http://dockerhost:8000
* **WebApp** : http://dockerhost:5000

## Nom des hosts 
La WebApp tente de joindre l'API sur le host quote-api:8000. 