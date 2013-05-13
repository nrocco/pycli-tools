.PHONY: build upload deps test bump clean

PY = $(VIRTUAL_ENV)/bin/python
PIP = $(VIRTUAL_ENV)/bin/pip
NOSE = $(VIRTUAL_ENV)/bin/nosetests
COVERAGE = $(VIRTUAL_ENV)/bin/coverage

current_version = $(shell $(PY) setup.py --version)
package_name = $(shell $(PY) setup.py --name)
init_py_file = $(package_name)/__init__.py


$(PY):
	virtualenv env
	$(eval VIRTUAL_ENV = $(PWD)/env)


# Build the source tarball
build: $(PY) test clean
	$(PY) setup.py sdist


# Prepare the environment for development
develop: $(PY) deps
	$(PY) setup.py develop


# Upload package to PyPi
upload: $(PY) test clean
	$(PY) setup.py sdist register upload


# install development dependencies
deps: $(PY)
	if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi


# run all tests with nosetests
test: $(PY) deps $(NOSE)
	$(NOSE)


coverage: $(PY) deps $(NOSE) $(COVERAGE)
	$(NOSE) --with-coverage --cover-package=$(package_name)


# install dependencies need for testing
$(NOSE): $(PY)
	$(PIP) install nose


# Install the coverage module
$(COVERAGE): $(PY)
	$(PIP) install coverage


# bump the version number
bump:
	@test ! -z "$(version)" || ( echo "specify a version number: make bump version=x.x.x" && exit 1 )
	@git status --porcelain 2> /dev/null | grep -v "^??" &&\
	  ( echo 'uncommited changes. commit them first' && exit 6 ) ||\
	  echo 'Bumping version'
	@echo "Bumping current version $(current_version) to $(version)"
	sed -i -e "/^__version__ = .*$$/s/'[^']*'/'$(version)'/" $(init_py_file)
	git add $(init_py_file)
	git commit -m 'Bumped version number to $(version)'
	git tag -m 'Mark stable release version $(version)' -a $(version)
	@echo "Version $(version) commited and tagged. You can push now :)"


# Clean all build artifacts
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '._*' -exec rm -f {} +
	find . -name '.coverage*' -exec rm -f {} +
	rm -rf build/ dist/ MANIFEST 2>/dev/null || true
