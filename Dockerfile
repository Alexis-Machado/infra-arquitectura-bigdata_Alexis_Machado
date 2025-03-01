# Usamos la imagen oficial de Python 3.9 como Base
FROM python:3.9

# Definimos el Directorio de Trabajo Dentro del Contenedor
WORKDIR /app

# Copiamos el Archivo de Dependencias (requirements.txt) al Contenedor
COPY requirements.txt .

# Instalamos las Dependencias sin Usar Caché para Reducir el Tamaño de la Imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el Código Fuente al Contenedor Dentro del Directorio /app/src
COPY src/ ./src

# Definimos el Comando de Inicio que Ejecutará el Script de Ingesta de Datos
CMD ["python", "src/bigdata/ingestion.py"]
