# Obtener imagen base
FROM --platform=linux/arm64 python:3.10.4-slim-bullseye

# Establecer variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

# Copiar proyecto
COPY . .