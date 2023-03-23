lint:
	pylint --recursive=y i18nx tests setup.py

test:
	pytest tests/*

coverage:
	pytest --cov=pi18n tests/*

clean:
	rm -rf dist/

dist: setup.py i18nx/*.py
	rm -rf dist/
	python -m build

publish: dist
	twine upload dist/*
