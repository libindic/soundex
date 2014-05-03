travis:
	nosetests -s --with-coverage --cover-package=silpa_common
	flake8 silpa_common tests

clean:
	find . -name "*.pyc" -exec rm -vf {} \;
	find -name __pycache__ -delete

tox:
	tox

flake:
	flake8 silpa tests
