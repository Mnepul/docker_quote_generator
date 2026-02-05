FROM python:3.14-alpine3.23

# Package python
COPY requirements.txt /var/requirements.txt
RUN pip install --no-cache-dir -r /var/requirements.txt

# On utilise /app pour l'application
WORKDIR /app
COPY app.py /app
COPY templates /app/templates/

EXPOSE 5000

CMD ["python3","app.py"]