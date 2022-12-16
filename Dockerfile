# Obtener imagen base
FROM python:3

# Establecer variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar proyecto
COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]