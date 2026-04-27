# HK Government Job Market Analysis

## Project Overview

This project analyzes real Hong Kong government job vacancy data to uncover salary patterns, department trends, and the impact of experience on compensation.

It demonstrates an end-to-end data workflow including data collection, cleaning, SQL analysis, and visualization.

---

## Summary

- Average salary: HKD 57,020  
- Salary range: HKD 11,500 – HKD 137,085  
- Highest paying departments: Lands Department, Department of Health, Fire Services Department  
- Salary increases with experience, with the largest jump from Entry to Mid level  

---

## Tools & Technologies

- Python (Requests, Pandas)
- SQL (SQLite)
- Excel (Data Visualization)
- GitHub (Project Presentation)

---

## Data Source

- Source: Hong Kong Government Open Data  
- URL: https://www.csb.gov.hk/datagovhk/gov-vacancies/

Raw JSON data is not included due to file size limitations.  
The dataset can be reproduced using the provided Python script.

---

## Data Dictionary

- jobname: Job title  
- deptnamejve: Department name  
- entrypay: Raw salary description  
- salary: Extracted numeric salary (HKD)  
- expfrom: Minimum years of experience  
- experience_level: Entry / Mid / Senior  
- salary_level: High (>=60000) / Low (<60000)  

---

## Key Insights

### Salary Overview

- Average monthly salary: HKD 57,020  
- Salary range: HKD 11,500 – HKD 137,085

  <img src="images/sql/1_overall_avg_salary.png" width="320">

---

### Top Paying Departments

- Lands Department (~HKD 119K)  
- Department of Health (~HKD 105K)  
- Fire Services Department (~HKD 99K)

<img src="images/excel/1_Top 10 HK GOV Departments by Average Monthly Salary.png" width="400">

---

### Salary vs Experience

- Salary increases with experience  
- Largest increase from Entry to Mid level

<img src="images/excel/3_Salary Growth by Experince Level.png" width="400">
---

## Visualizations

### Top 10 Departments by Salary

Top 10 Departments

High-paying roles are concentrated in technical and specialized departments.

<img src="images/sql/3_top_10_departments_by_avg_salary.png" width="320">

<img src="images/excel/1_Top 10 HK GOV Departments by Average Monthly Salary.png" width="400">

---

### Salary Distribution

Salary Distribution

Most job opportunities are concentrated in the mid-salary range.

<img src="images/sql/4_avg_salary_by_experience_level.png" width="320">

<img src="images/excel/4_Salary Distribution by Experience Level.png" width="400">

---

### Salary by Experience

Salary by Experience

Salary growth is strongest from Entry to Mid level.

<img src="images/sql/6_salary_level_distribution.png" width="320">

---

### High vs Low Salary by Experience

Salary Level

Higher experience levels are associated with a greater proportion of high-paying roles.

<img src="images/sql/7_experience_level_vs_salary_level.png" width="320">

---

## SQL Analysis

These SQL queries are used to validate and support the insights shown in the visualizations.

Example:

SELECT experience_level, AVG(salary)
FROM gov_jobs
GROUP BY experience_level;

Full queries available in:

sql/analysis.sql

---

## Business Value

This analysis helps identify:

- Which departments offer higher salary potential  
- How experience affects earning potential  
- Where most job opportunities are concentrated  

---

## How to Reproduce

pip install -r requirements.txt  
python scripts/fetch_data.py  
python scripts/sql_analysis.py  

---

## Author

Freda Choy
