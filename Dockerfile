FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Apply migrations, create a superuser, and run the server
CMD ["sh", "-c", "python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py create_admin && \
    python manage.py runserver 0.0.0.0:8000"]
