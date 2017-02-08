.PHONY: clean-pyc install docs

all: clean-pyc install

install:
	pip install -r requirements.txt
	python3 setup.py install

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -rf build dist translator.egg-info tests/__pycache__ translator/__pycache__

docs:
	$(MAKE) -C docs html
