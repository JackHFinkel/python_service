run:
	cd app && uvicorn main:app --reload

build:
	pip freeze > requirements.txt
	-docker-compose down # ignore if cannot take down container. Will not work first time
	-docker volume rm python-service_db-data # ignore if cannot remove volume. Will not work first time
	docker compose up --build  