# Main Python file variable

main_py_file = src/main.py

# Running the project

run_project:
	python3 $(main_py_file)

# Unit tests

pytest = python3 -m pytest
unit_tests_file = test/test_main.py
check_cov = $(pytest) --cov=src.main --cov-fail-under=80

run_all_unit_tests:
	$(pytest) $(unit_tests_file)

run_specific_unit_test:
	$(pytest) $(unit_tests_file)::$(TEST_NAME)

run_specific_unit_tests:
	$(pytest) $(addprefix $(unit_tests_file)::,$(TEST_NAMES))

check_cov:
	$(check_cov)

check_cov_with_report:
	$(check_cov) --cov-report json

# Style

black = python3 -m black

style_all_files:
	$(black) .

check_style:
	$(black) --check .

# Documentation

check_docs:
	pydocstyle $(main_py_file)

generate_docs:
	pdoc $(main_py_file) -o ./docs

# Cyclomatic complexity

cc = python3 -m radon cc
cc_paths = src test

complexity:
	$(cc) $(cc_paths)

complexity_check:
	[ -z "$$($(cc) -n D $(cc_paths))" ]

# Update Docker image

update_docker_image:
	docker buildx build --push -t antoinebrunet1/word_reactor_pipeline .