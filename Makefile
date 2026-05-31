# Main Python file variable

main_py_file = src/main.py

# Running the project

run_project:
	python3 $(main_py_file)

# Unit tests

pytest_cmd = python3 -m pytest
unit_tests_file = test/test_main.py
run_all_unit_tests_cmd = $(pytest_cmd) $(unit_tests_file)
check_cov_cmd = $(pytest_cmd) --cov=src.main --cov-fail-under=80

run_all_unit_tests:
	$(run_all_unit_tests_cmd)

run_specific_unit_test:
	$(run_all_unit_tests_cmd)::$(TEST_NAME)

run_specific_unit_tests:
	$(pytest_cmd) $(addprefix $(unit_tests_file)::,$(TEST_NAMES))

check_cov:
	$(check_cov_cmd)

check_cov_with_report:
	$(check_cov_cmd) --cov-report json

# Style

black_cmd = python3 -m black

style_all_files:
	$(black_cmd) .

check_style:
	$(black_cmd) --check .

# Documentation

check_docs:
	pydocstyle $(main_py_file)

generate_docs:
	pdoc $(main_py_file) -o ./docs

# Cyclomatic complexity

cc_cmd = python3 -m radon cc
cc_paths = src test

complexity:
	$(cc_cmd) $(cc_paths)

complexity_check:
	[ -z "$$($(cc_cmd) -n D $(cc_paths))" ]

# Docker push

docker_push:
	docker buildx build --push -t antoinebrunet1/word_reactor_pipeline .