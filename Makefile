up-dev:
	pip3.11 install pip --upgrade
	pip install -r requirements/develop.txt
	cp ./devtools/dotenv.dev .env
	cd app/ && . ../entrypoint.sh

	

up-prod:
	pip3.11 install pip --upgrade
	pip install -r requirements.txt
	cp ./devtools/dotenv.prod .env
	cd app/ && . ../entrypoint.sh

down:
	docker compose down

clean:
	docker compose down
	docker rmi brain-agri-django_gunicorn
	docker rmi brain-agri-nginx
	docker rmi postgres
	docker volume rm brain-agri_db-pg-data
	docker volume rm brain-agri_static
	