FROM python:3.14-alpine3.23

# package pythons
COPY requirements.txt /var/requirements.txt
RUN pip install --no-cache-dir -r /var/requirements.txt

# On utilise /app pour l'application    
WORKDIR /app
COPY main.py main.py
COPY quotes.txt quotes.txt

# On expose le port 
EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]