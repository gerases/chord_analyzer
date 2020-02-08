MODULE_NAME:=chord_finder
PYTHON_VER:=3.6

# Get the abs path of the Makefile
MKFILE_PATH:=$(abspath $(lastword $(MAKEFILE_LIST)))

# Get the dir component
MKDIR:=$(dir $(MKFILE_PATH))

# Remove trailing slash
MKDIR:=$(patsubst %/,%,$(MKDIR))

ENV_PATH:=$(MKDIR)/env

# pip install --editable will cause an egg link to be
# installed under under site-packages of the environment.
# In addition, all the requirements defined in setup.py will
# be installed. As a result, all of the code and tests will
# be able to have access to the module without further
# modifications to sys.path.
#
# When the module is installed this way,
# <MODULE_NAME>.egg-info dir is dropped and it's one of the
# ways I can think of as as an indication that pip install
# --editable has been run.
$(MODULE_NAME).egg-info: $(ENV_PATH) setup.py
	@env/bin/pip install --editable .

.PHONY: unit
unit: $(MODULE_NAME).egg-info
	@env/bin/pytest -vra $(testargs)

.PHONY: egg
egg: $(ENV_PATH)
	@env/bin/python setup.py bdist_egg

.PHONY: rpm
rpm: $(ENV_PATH)
	@env/bin/python setup.py bdist_rpm

.PHONY: env
env: $(ENV_PATH)

$(ENV_PATH):
	@echo Building development Python environment
	@rm -rf $(MKDIR)/env
	@virtualenv --python=python$(PYTHON_VER) env
	@env/bin/pip install --upgrade --no-cache-dir pip setuptools
	@env/bin/pip install --upgrade --no-cache-dir pytest sh pylint pytest-mock flake8
	@echo
	@echo Python environment built, to enable run the following:
	@echo
	@echo "  source env/bin/activate"
	@echo

.PHONY: clean
clean:
	@rm -rf $(MKDIR)/env
	@rm -rf $(MKDIR)/build
	@rm -rf $(MKDIR)/dist
	@rm -rf $(MKDIR)/$(MODULE_NAME).egg-info
