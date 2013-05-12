.PHONY: build upload deps test bump

VIRTUAL_ENV ?= /usr
PY = $(VIRTUAL_ENV)/bin/python
PIP = $(VIRTUAL_ENV)/bin/pip
NOSE = $(VIRTUAL_ENV)/bin/nosetests


# Build the source tarball
build:
	$(PY) setup.py sdist


# Upload package to PyPi
upload:
	$(PY) setup.py sdist register upload


# install development dependencies
deps:
	if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi


# run all tests with nosetests
test: nose
	$(NOSE)


# install dependencies need for testing
nose: $(NOSE)
	$(PIP) install nose


# bump the version number
bump:
	@test ! -z "$(version)" || ( echo "specify a version number: make bump version=x.x.x" && exit 1 )
	@git status --porcelain 2> /dev/null | grep -v "^??" &&\
	  ( echo 'uncommited changes. commit them first' && exit 6 ) ||\
	  echo 'Bumping version'
	sed -i -e "/^__version__ = .*$$/s/'[^']*'/'$(version)'/" pycli_tools/__init__.py
	git add pycli_tools/__init__.py
	git commit -m 'Bumped version number to $(version)'
	git tag -m 'Mark stable release version $(version)' -a $(version) 
	@echo "Version $(version) commited and tagged. You can push now :)"
