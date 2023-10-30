# Python tasks
install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python3 -m pytest -vv --cov=main test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

# Rust tasks
build-rust:
	cargo build --release

all: install lint format test build-rust
