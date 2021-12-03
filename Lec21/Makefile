.PHONY: format, lint, check

lint:
	pylint main.py

format:
	black main.py && docformatter -i main.py && isort main.py

check:
	mypy main.py

.DEFAULT_GOAL := format