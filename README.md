# Employee Data Analysis - Week 1 Day 5


## About the Project


This project is part of my Python and Data Engineering training.


I used a small employee dataset to practice data cleaning, salary analysis, and data visualization.


## Dataset


The employees.csv file contains 8 employees.


Columns:
id
name
department
salary
city
## Tools Used


Python
Pandas
Matplotlib
Jupyter Notebook
VS Code
## Work Completed


### 1. Data Cleaning


Checked missing values and duplicate records
Standardized text columns
Converted numeric columns
Checked salary outliers using IQR
Saved the cleaned data as clean_data.csv
The original dataset had 8 rows, no missing values, and no duplicates.


### 2. Data Analysis


Calculated salary statistics
Compared departments and cities
Checked numeric correlations
Answered five business questions
Merged sample department budget data
Created a pivot table
### 3. Data Visualization


Created five charts:
1. Average salary by department
2. Salary distribution
3. Employee ID vs Salary
4. Sorted employee salaries
5. Salary box plot


All charts are saved in reports/figures/.


## Key Findings


Finance has the highest average salary of INR 90,000.
Chennai has the most employees, with 4 employees.
Salaries range from INR 30,000 to INR 90,000.
## How to Run


1. Install Python and VS Code.
2. Open the project folder.
3. Install the packages using:


   pip install -r requirements.txt


4. Run the Python files in this order:


   python day5_data_cleaning.py


   python day5_analysis.py


   python day5_visualization.py


5. Open day5_project.ipynb in Jupyter Notebook.
6. Run the notebook cells from top to bottom.


## Limitations


This project uses only 8 employee records.
The department budgets are sample values.
A larger dataset would provide more reliable results.