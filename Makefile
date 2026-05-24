# Variables (Beginning)

main_py_file = src/main.py
unit_tests_file = test/test_main.py
check_cov_cmd = python3 -m pytest --cov=src.main --cov-fail-under=80
run_all_unit_tests_cmd = python3 -m pytest $(unit_tests_file)

# Variables (End)

# Running the project (Beginning)

run_project:
	python3 $(main_py_file)

# Running the project (End)

# Unit tests (Beginning)

run_all_unit_tests:
	$(run_all_unit_tests_cmd)

run_specific_unit_test:
	$(run_all_unit_tests_cmd)::$(TEST_NAME)

run_specific_unit_tests:
	python3 -m pytest $(foreach T,$(NAMES),$(unit_tests_file)::$(T))

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
	pydocstyle $(main_py_file)

generate_docs:
	pdoc $(main_py_file) -o ./docs

# Documentation (End)