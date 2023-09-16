.PHONY: build, run

IMAGE_NAME = "app_crud_python"

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --rm $(IMAGE_NAME)