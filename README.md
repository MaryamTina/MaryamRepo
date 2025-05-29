# Customer Data Display Project

A web application for displaying customer data from a JSON file, integrated with a robust CI/CD pipeline using GitHub Actions. This project fulfills academic requirements for automated data processing, testing, and deployment.

## Overview
This repository (`MaryamTina/MaryamRepo`) hosts a web application that showcases customer data in a tabular format. It leverages Python for data generation and transformation, JavaScript for frontend rendering, and GitHub Actions for continuous integration and deployment to GitHub Pages.

## Features
- **Data Generation**: Creates synthetic customer data (`profiles1.csv`) using `generate.py` with the `Faker` library.
- **Data Transformation**: Converts CSV to JSON (`data.json`) via `csvtojson.py` for web consumption.
- **Web Interface**: Renders data in a responsive table using `index.html` and `script.js`.
- **CI/CD Pipeline**: Automates testing and deployment through `main.yml`, ensuring reliable updates to GitHub Pages.
- **Unit Testing**: Validates data integrity with `calculateTests.py` (business logic) and `test_data.py` (CSV/JSON validation).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/MaryamTina/MaryamRepo