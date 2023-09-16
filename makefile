.PHONY: build, run, compose, down

IMAGE = "app_crud_python"

build:
	docker build -t $(IMAGE) .

compose:
	docker compose up -d
	docker compose exec cli /bin/bash

down:
	docker compose down

run:
	docker run -it --rm $(IMAGE)