e2e:
	python3 scripts/generate_readiness_matrix.py

test:
	python3 -m pytest -q
