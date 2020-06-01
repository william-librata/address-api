SHELL := /bin/bash

init:

	# update cache
	sudo apt-get update; \

	# install software
	sudo apt-get install libpq-dev -y; \
	sudo apt-get install curl -y; \
	sudo apt-get install autoconf -y; \
	sudo apt-get install automake -y; 
	sudo apt-get install libtool -y; \
	sudo apt-get install python-dev -y; \
	sudo apt-get install pkg-config -y; \
	sudo apt-get install apache2 -y; \
	sudo apt-get install apache2-dev -y; \

	# install libpostal
	libpostal_dir=/usr/src/libpostal; \
	libpostal_data_dir=/usr/src/libpostal_data; \
	current_dir=$$PWD; \
	sudo rm -rf $$libpostal_dir; \
	sudo rm -rf $$libpostal_data_dir; \
	sudo git clone https://github.com/openvenues/libpostal $$libpostal_dir; \
	cd $$libpostal_dir; \
	sudo ./bootstrap.sh; \
	sudo ./configure --datadir=$$libpostal_data_dir; \
	sudo make; \
	sudo make install; \
	sudo ldconfig; \
	cd $$current_dir; \

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

.PHONY: init test
