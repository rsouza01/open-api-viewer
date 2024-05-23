.DEFAULT_GOAL := help
.PHONY: all build run test utest


help:
	@echo 'Available commands:'
	@echo -e 'run \t\t - \t Executes script'

run: 
	python ./src/apiviewer.py
