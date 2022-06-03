.PHONY: build venv deps clean release test check install_codecov_binary coveralls docs

build: venv deps develop

venv:
	virtualenv -p python3 .env
	
deps:
	.env/bin/pip install -r requirements_dev.txt
	.env/bin/pip install -r requirements_dev_backend.txt

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

release:
	git push; git push --tags; rm dist/*; python3 setup.py clean sdist; twine upload dist/*


check:
	python setup.py check -s pylint setup.py scrapx tests 


docs:
	if [ -e docs/_build ]; then rm -r docs/_build; fi \
		&& sphinx-build -b html docs docs/_build