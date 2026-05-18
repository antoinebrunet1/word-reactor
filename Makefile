run:
	python3 main.py

style_all_files:
	python3 -m black .

check_style:
	python3 -m black --check .

check_docs:
	pydocstyle main.py

check_cov:
	python3 -m pytest --cov=main --cov-fail-under=80