# Usar una imagen base de Python
FROM python:3.9

ENV FILES ./files

# Establecer el directorio de trabajo en el contenedor
WORKDIR /api

# Copiar el archivo de requisitos y instalar los paquetes necesarios
COPY $FILES/src/requirements.txt .
# Certificados para desarrollo comentar en producción para usar certbot y rebuild image
COPY $FILES/cert/ /api/cert  
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación en el contenedor
COPY ./files/src .

# Definir el comando para ejecutar la aplicación
CMD ["uwsgi", "--ini", "uwsgi.ini"]