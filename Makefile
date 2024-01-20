all: style

style:
	isort .
	black .
	ruff check .
