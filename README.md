# BackendCulturameta


## Clonar el repositorio

```bash
git clone https://github.com/Jorgecuenca1/BackendCulturameta.git
```

### Configuración del proyecto en local

* Crear un archivo .env basado en el archio .env.template, modificar las variables declaradas en el archivo .env a su gusto, se recomienda usar un generador para el secret key (https://djecrety.ir/).

* Hacer build
```bash
docker-compose build
```

### Correr el proyecto en local

```bash
docker-compose up
```

### Comandos de Django

En el archivo Makefile se encuentran algunos de los comandos comunes del framework, para ejecutarlos deberá escribir en la consola `make` y luego el nombre del comando:

* Construir y aplicar migraciones:
    ```bash
    make migrate
    ```
* Crear super usuario:
    ```bash
    make superuser
    ```
* Colectar archivos estáticos:
    ```bash
    make statics
    ```

En caso de no estar el comando que desea lanzar, podrá hacerlo de la siguiente forma:

* Si el proyecto está corriendo con `docker-compose up`
```bash
docker-compose exec culturameta python manage.py -h
```

* Si el proyecto no está corriendo con `docker-compose up`
```bash
docker-compose run --rm culturameta python manage.py -h
```