# Documentación Proyecto API Prima.law

### Miguel Eduardo Guevara, PhD
### Luis Bedoya
### John Wick
### Luis Tombe Arcos  

# Introducción

Se creo un template para el deploy de la API usando Python con la libreria Grafene en Flask framework

Hay dos templates de configuración uno de desarrollo por defecto y uno de producción para replicar en la instancia que se integrara al proyecto.

El proyecto usa Flask como servidor de DEV pero para la presentacion del servicio y seguridad usa uWSGI presentado como servicio via proxy inverso por NGINX

El template de desarrollo usa mkcert para crear certificados falsos para el ambiente local y se definio una URL de prueba **api.local**

```console
mkcert api.local "*.api.local" localhost 127.0.0.1 ::1\n
```

en el directorio **files** se crean todas las configuraciones del sistema en la respectiva carpeta: 

cert --> certificados falsos para dev
certbot --> certificados para producción
nginx --> configuración NGINX
src --> fuentes del proyecto desarrollo API

Para levantar el proyecto con docker compose

```console
docker compose up --build
```

Para consultar la respuesta de la API

```url
https://localhost
```

# NOTAS:

Para crear los certificados en producción:

```console
docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d api.prima.law
```

Para renovar los certificados:

```console
docker compose run --rm certbot renew
```

Renombrar los archivos de docker-compose para hacer el build correspondiente.
