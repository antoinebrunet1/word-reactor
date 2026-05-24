# Variables (Beginning)

check_cov_cmd = python3 -m pytest --cov=src.main --cov-fail-under=80
run_all_tests_cmd = python3 -m pytest test/test_main.py

# Variables (End)

# Running the project (Beginning)

run:
	python3 src/main.py

# Running the project (End)

# Unit tests (Beginning)

run_all_tests:
	$(run_all_tests_cmd)

run_specific_unit_test:
	$(run_all_tests_cmd)::$(TEST_NAME)

run_specific_unit_tests:
	python3 -m pytest $(foreach T,$(NAMES),test/test_main.py::$(T))

check_cov:
	$(check_cov_cmd)

check_cov_with_report:
	$(check_cov_cmd) --cov-report json

# Unit tests (End)

# Style (Beginning)

style_all_files:
	python3 -m black .

check_style:
	python3 -m black --check .

# Style (End)

# Documentation (Beginning)

check_docs:
	pydocstyle src/main.py

generate_docs:
	pdoc src/main.py -o ./docs

# Documentation (End)