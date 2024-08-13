# recipe-app-api
Recipi Api Project

# Comandos docker
# Construir imagen docker
docker-compose build

# Habilitar linting de flake8
docker-compose run --rm app sh -c "flake8"

# Construir proyecto de Django
docker-compose run --rm app sh -c "django-admin startproject app ."

# Levantar microservicio
docker-compose up

# Ejecutar pruebas
docker-compose run --rm app sh -c "python manage.py test"


# Ejecutar core app
docker-compose run --rm app sh -c "python manage.py startapp core"