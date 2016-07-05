WITH_ENV = env `[ -n "$$WEB_PORT_5000_TCP_PROTO" ] && echo || cat .env 2>/dev/null | xargs`

COMMANDS = help clean install-deps compile-deps 

help:
	@echo 'commands: $(COMMANDS)'

clean:
	@find . -name '*.pyc' -type f -delete
	@find . -name '__pycache__' -type d -delete
	@find . -type d -empty -delete

compile-deps:
	@pip-compile requirements.in
	@pip-compile requirements-dev.in
	@pip-compile requirements-testing.in

install-deps:
	@[ -n "$(VIRTUAL_ENV)" ] || (echo 'out of virtualenv'; exit 1)
	@pip install -U pip setuptools
	@pip install -r requirements.txt
	@pip install -r requirements-dev.txt
	@pip install -r requirements-testing.txt

lint:
	@echo "[lint:py] basic"
	@$(WITH_ENV) flake8 --immediate
	@echo "[lint:py] complexity (warning only)"
	@$(WITH_ENV) flake8 --immediate --max-complexity=24 core sky || true
