# Polars Descriptive Statistics Script
[![CI](https://github.com/Jingzhi-cyber/jz422-IDS706-Week3-Polars/actions/workflows/cicd.yml/badge.svg)](https://github.com/Jingzhi-cyber/jz422-IDS706-Week3-Polars/actions/workflows/cicd.yml)

This repository sets up an environment on CodeSpaces and uses GitHub Actions to run a Makefile for the following commands: make install, make test, make format, and make lint.

## Getting Started
To set up the project, simply run make all or run make install and make test.
![Alt text](image_make.png)

## Features
### Data Analysis
Included is a Python script data_analysis.py that performs basic data analysis tasks using Polars:

- Reads a dataset from a CSV file
- Generates summary statistics like mean, median, and standard deviation
- Creates a histogram for a specified column in the dataset

### How to Use the Data Analysis Script
1. Place your CSV file in the same directory as the script or update the file_path variable in the script to point to your CSV file.
2. Run the script:

    **python3 data_analysis.py**

3. Check the output for summary statistics and look for the generated histogram image in the current directory.
![Alt text](image_terminal.png)

![Alt text](Average_histogram.png)

![Alt text](image_report.png)

## Test CSV File: hurricanes.csv

I get it from <https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html>
![Alt text](image_csv.png)

## Project Structure
- **.devcontainer** includes a Dockerfile and devcontainer.json. The **Dockerfile** within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.
- **workflows** includes GitHub Actions, which contain configuration files for setting up automated build, test, and deployment pipelines for your project.
- **.gitignore** is used to specify which files or directories should be excluded from version control when using Git.
- **Makefile** is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.
- **README.md** is the instruction file for the readers.
- **requirements.txt** is to specify the dependencies (libraries and packages) required to run the project.
- **test_main.py** is a test file for main.py that can successfully run in IDEs.
- **main.py** is a Python file that contains the main function.
- **data_analysis.py** is a Python script for basic data analysis tasks using Polars.
