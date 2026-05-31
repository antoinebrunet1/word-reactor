# Variables

main_py_file = src/main.py
unit_tests_file = test/test_main.py
check_cov_cmd = python3 -m pytest --cov=src.main --cov-fail-under=80
run_all_unit_tests_cmd = python3 -m pytest $(unit_tests_file)
black_cmd = python3 -m black
cc_cmd = python3 -m radon cc
cc_paths = src/ test/
docker_image_name = antoinebrunet1/word_reactor_pipeline

# Running the project

run_project:
	python3 $(main_py_file)

# Unit tests

run_all_unit_tests:
	$(run_all_unit_tests_cmd)

run_specific_unit_test:
	$(run_all_unit_tests_cmd)::$(TEST_NAME)

run_specific_unit_tests:
	python3 -m pytest $(addprefix $(unit_tests_file)::,$(TEST_NAMES))

check_cov:
	$(check_cov_cmd)

check_cov_with_report:
	$(check_cov_cmd) --cov-report json

# Style

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

complexity:
	$(cc_cmd) $(cc_paths)

complexity_check:
	[ -n $($(cc_cmd) --min D $(cc_paths)) ]

# Docker push

docker_push:
	docker build -t $(docker_image_name) .
	docker login
	docker push $(docker_image_name)