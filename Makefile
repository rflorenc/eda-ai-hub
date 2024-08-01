SHELL = /usr/bin/env bash -o pipefail
.PHONY: default test venv venv-clean clean clean-all

WORKDIR?=.
PY?=python3
VENVDIR?=$(WORKDIR)/venv
VENV=$(VENVDIR)/bin

.EXPORT_ALL_VARIABLES:

default: venv

dev: clean

clean: venv-clean

venv-clean:
	rm -fr $(VENVDIR)

# Prepare a Python3 virtualenv.
venv:
	$(PY) -m venv --prompt venv $(VENVDIR)
	$(VENV)/pip install --upgrade pip
	$(VENV)/pip install -Ur requirements.txt pip

requirements:
	$(PY) -m pip install -r requirements.txt

# Tests
# test:
# 	$(PY) -m unittest test/test.py