.PHONY: build upload deps test bump clean docs upload_docs

VIRTUAL_ENV ?= $(PWD)/env

PY = $(VIRTUAL_ENV)/bin/python
PIP = $(VIRTUAL_ENV)/bin/pip
NOSE = $(VIRTUAL_ENV)/bin/nosetests
COVERAGE = $(VIRTUAL_ENV)/bin/coverage
SPHINXBUILD = $(VIRTUAL_ENV)/bin/sphinx-build

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


# Generate documentation
docs: $(PY) $(SPHINXBUILD)
	cd docs/; $(MAKE) html SPHINXBUILD=$(SPHINXBUILD)


$(SPHINXBUILD):
	$(PIP) install sphinx


# Upload package to PyPi
upload: $(PY) test clean
	$(PY) setup.py sdist register upload


# Upload Sphinx documentation to http://pythonhosted.org
upload_docs: $(PY) test clean docs
	$(PY) setup.py upload_docs --upload-dir docs/_build/html/


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
bump: $(PY)
	@test ! -z "$(version)" || ( echo "specify a version number: make bump version=$(current_version)" && exit 1 )
	@! git status --porcelain 2> /dev/null | grep -v "^??" || ( echo 'uncommited changes. commit them first' && exit 1 )
	@echo "Bumping current version $(current_version) to $(version)"
	sed -i '.bak' -e "/^__version__ = .*$$/s/'[^']*'/'$(version)'/" $(init_py_file)
	rm -f $(init_py_file).bak
	git add $(init_py_file)
	git commit -m 'Bumped version number to $(version)'
	git tag -m 'Mark stable release version $(version)' -a $(version)
	@echo "Version $(version) commited and tagged. You can 'make push' now :)"


# Push to github but run tests first
push: test
	git push origin HEAD
	git push origin --tags


# Clean all build artifacts
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '._*' -exec rm -f {} +
	find . -name '.coverage*' -exec rm -f {} +
	rm -rf build/ dist/ MANIFEST docs/_build/* 2>/dev/null || true
