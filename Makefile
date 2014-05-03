travis:
	nosetests -s --with-coverage --cover-package=soundex
	flake8 soundex tests

clean:
	find . -name "*.pyc" -exec rm -vf {} \;
	find -name __pycache__ -delete

tox:
	tox

flake:
	flake8 silpa tests
