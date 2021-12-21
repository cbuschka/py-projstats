TOP_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL := /bin/bash

run:	init
	@source ${TOP_DIR}/.venv/bin/activate && \
	python3 -B -m projstats

build:	init

init:
	@if [ ! -d "${TOP_DIR}/.venv/" ]; then \
		virtualenv -p python3 ${TOP_DIR}/.venv/ && \
		source ${TOP_DIR}/.venv/bin/activate && \
		pip install -r ${TOP_DIR}/requirements.txt; \
	fi

install_deps:	init
	@source ${TOP_DIR}/.venv/bin/activate && \
	pip install -r ${TOP_DIR}/requirements.txt
