
## Docker
# Налаштування .env

Створіть файл .env в /.env
і вставте код, що йде нижче
====== початок .env ===================

SECRET_KEY = django-insecure-5j(*k)&t+&_uk)(h86$$e-$&8i*%@_%bh@bt!n)e211+v37_%d


DEBUG = True

ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0


DB_ENGINE=postgres
DB_NAME=test_order
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=db
DB_PORT=5432


====== кінець .env ===================

====================================
python manage.py check --settings=config.settings

docker compose up --build

docker compose down

docker compose down -v

docker compose exec web python manage.py createsuperuser


Також потрібен requirements.txt з усіма залежностями.


 .env файл. DB_HOST має бути db (назва сервісу в compose), не localhost

 docker compose up --build

 docker compose logs web

 docker compose down