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

t:
	cd app/ && . ../entrypoint.sh
	
	
	
	