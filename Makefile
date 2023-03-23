test:
	pytest tests/*

coverage:
	pytest --cov=pi18n tests/*

build:
	python -m build

publish:
	python -m twine upload -r testpypi dist/*
