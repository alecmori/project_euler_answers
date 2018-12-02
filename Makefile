all: venv cython

cython:
	python setup.py build_ext --inplace

readme: venv
	for i in {1..25}; do\
		python -m readme2tex \
			--output answers/problem_$$i/rationale.md \
			answers/problem_$$i/rationale_in_latex.md; \
		done

run_all: venv cython
	python utils/run_all_problems.py

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
