lint:
	pylint --recursive=y i18nx tests setup.py

test:
	pytest tests/*

coverage:
	pytest --cov=pi18n tests/*

clean:
	rm -rf dist/

dist: i18nx/*.py
	python -m build

publish: dist
	twine upload -r testpypi dist/*
