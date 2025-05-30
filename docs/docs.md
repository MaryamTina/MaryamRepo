# Project Documentation

## Requirements
- **Requirements**: Public repository, unit tests, CI/CD pipeline, GitHub Pages deployment.
- **Requirements**: Branching strategy, CSV-to-JSON conversion, advanced tests for CSV/JSON.

## Challenges
- Configuring GitHub Pages and resolving initial pipeline failures.
- Ensuring consistent data between `profiles1.csv` and `data.json`.
- Managing file placement (e.g., moving files from `__pycache__`).

## Solutions
- Used `Faker` library for realistic data generation in `generate.py`.
- Implemented debug mode in `csvtojson.py` to catch errors.
- Developed `test_data.py` with tests for CSV columns, rows, and JSON properties.
- Created branches (`pipeline`, `tests`) for organized development.

## Lessons Learned
- Importance of proper file organization and `.gitignore` for clean repositories.
- Debugging CI/CD pipelines requires checking logs and dependencies.
- Branching improves collaboration and isolates feature development.

## Future Improvements
- Add more robust data validation (e.g., format checks for dates, phone numbers).
- Implement a search/filter feature in the web interface.
- Expand test coverage for edge cases in `generate.py`.

## Repository Structure

MaryamRepo/
├── .github/
│   └── workflows/
│       └── main.yml          
├── docs/
│   ├── actions_screenshot.png 
│   └── docs.md               
├── __pycache__/             
│   ├── calculate.cpython-310.pyc
│   └── calculate.cpython-312.pyc
├── .gitignore                
├── LICENSE                   
├── README.md                 
├── calculate.py              
├── calculateTests.py        
├── csvtojson.py              
├── data.json                 
├── generate.py               
├── index.html                
├── main.py                   
├── profiles1.csv             
├── script.js                 
└── test_data.py              