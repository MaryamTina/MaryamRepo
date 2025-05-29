# Project Documentation

## Requirements
- **G-Requirements**: Public repository, unit tests, CI/CD pipeline, GitHub Pages deployment.
- **VG-Requirements**: Branching strategy, CSV-to-JSON conversion, advanced tests for CSV/JSON.

## Challenges
- Configuring GitHub Pages and resolving initial pipeline failures.
- Ensuring consistent data between `profiles1.csv` and `data.json`.
- Managing file placement (e.g., moving files from `__pycache__`).

## Solutions
- Used `Faker` library for realistic data generation in `generate.py`.
- Implemented debug mode in `csvtojson.py` to catch errors.
- Developed `test_data.py` with tests for CSV columns, rows, and JSON properties.
- Created branches (`pipeline`, `tests`) for organized development.