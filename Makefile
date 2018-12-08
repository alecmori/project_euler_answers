all: venv cython

check_answers: cython
	pytest tests/answers/correct_answers_test.py

cython:
	python setup.py build_ext --inplace

run_all: venv cython
	python utils/run_all_problems.py -n 1

venv:
	virtualenv venv --python=python3.6
	venv/bin/pip install -r requirements-minimal.txt
	touch venv/bin/activate

clean:
	rm -rf venv
	rm -rf answers/*/*.c
	rm -rf answers/*/__pycache__
	rm -rf answers/*/*.so
	rm -rf utils/proj_eul_math/*.c
	rm -rf utils/proj_eul_math/__pycache__
	rm -rf utils/proj_eul_math/*.so
	rm -rf build
