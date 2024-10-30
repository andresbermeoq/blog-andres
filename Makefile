DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: clean
clean:  ## Remove all temporary files like pycache
	find . -name \*.rdb -type f -ls -delete
	find . -name \*.pyc -type f -ls -delete
	find . -name __pycache__ -ls -delete
