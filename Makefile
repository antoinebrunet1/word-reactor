check_cov_cmd = python3 -m pytest --cov=src.main --cov-fail-under=80
run_all_tests_cmd = python3 -m pytest test/test_main.py

run:
	python3 src/main.py

run_all_tests:
	$(run_all_tests_cmd)

run_specific_test:
	$(run_all_tests_cmd)::$(TEST_NAME)

style_all_files:
	python3 -m black .

check_style:
	python3 -m black --check .

check_docs:
	pydocstyle src/main.py

check_cov:
	$(check_cov_cmd)

check_cov_with_report:
	$(check_cov_cmd) --cov-report json

generate_docs:
	pdoc src/main.py -o ./docs