VENV = .venv
PYTHON = python3
PIP = $(VENV)/bin/pip   

init: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	
	touch .env

