.PHONY: build, run, compose, compose-down

IMAGE_NAME = "app_crud_python"

build:
	docker build -t $(IMAGE_NAME) .

compose:
	docker compose up -d
	docker compose exec cli /bin/bash

down:
	docker compose down

run:
	docker run -it --rm $(IMAGE_NAME)