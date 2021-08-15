migrate:
	docker-compose exec culturameta python manage.py makemigrations
	docker-compose exec culturameta python manage.py migrate

requirements:
	docker-compose exec culturameta pip install -r requirements.txt

statics:
	docker-compose exec culturameta python manage.py collectstatic --no-input

superuser:
	docker-compose exec culturameta python manage.py createsuperuser

app:
	docker-compose exec culturameta python manage.py startapp $(APP_NAME)

logs:
	docker-compose logs -f -t --tail=$(lines) $(service)

mergemigrations:
	docker-compose exec culturameta python manage.py makemigrations --merge

test:
	docker-compose exec culturameta python manage.py test

makemessages:
	docker-compose exec culturameta python manage.py makemessages -l es

compilemessages:
	docker-compose exec culturameta python manage.py compilemessages -f

flake:
	docker-compose exec culturameta flake8

reset:
	docker-compose down -v
	rm -rf ./postgres-data

clean:
	rm -rf src/*/migrations/00**.py
	find . -name "*.pyc" -exec rm -- {} +
	rm -rf src/*/migrations/__pycache__/*