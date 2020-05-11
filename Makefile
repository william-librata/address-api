SHELL := /bin/bash

init:
	# update cache
	sudo apt-get update
	# install software
	sudo apt-get install libpq-dev -y
	# source venv
	source env/bin/activate; \
	# install all necessary packages
	pip3 install --upgrade wheel; \
	pip3 install --upgrade setuptools; \
	pip3 install -r requirements.txt; \

test:
	. env/bin/activate; \
	# run unit test
	python3 -m unittest discover tests; \

docs:
	# create html documentation using sphinx
	cd docs && make html; \

erd:
	java -jar bin/schemaSpy_5.0.0.jar -t pgsql -db places -host localhost -s public -u etl_user -p password -o erd -dp bin/postgresql-42.2.2.jar

.PHONY: init test docs install erd
