# HK Government Job Market Analysis

## Project Overview

This project analyzes real Hong Kong government job vacancy data to understand salary trends, department differences, and the impact of experience on compensation.

The goal is to demonstrate practical data analysis skills using Python, SQL, and Excel with a real-world dataset.

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

## Key Insights

### Salary Overview

- Average monthly salary: HKD 57,020  
- Salary range: HKD 11,500 – HKD 137,085  

This indicates a wide variation across job levels and roles.

---

### Top Paying Departments

- Lands Department (~HKD 119K)  
- Department of Health (~HKD 105K)  
- Fire Services Department (~HKD 99K)  

These roles are typically technical or professional positions.

---

### Salary vs Experience

- Salary increases with experience  
- The largest increase occurs between Entry to Mid level  
- Salary growth becomes more stable at Senior level  

---

### Salary Distribution

- Most jobs fall within HKD 20K – 50K  
- High-paying jobs are fewer but significantly higher  

---

### High vs Low Salary Analysis

- Entry-level roles are mostly low-paying  
- Mid and Senior roles have a higher proportion of high-paying jobs  
- Experience plays a key role in accessing higher salary opportunities  

---

## Visualizations

### Top 10 Departments by Salary  
Top10

### Salary Distribution  
Distribution

### Salary by Experience  
Experience

### High vs Low Salary by Experience  
Salary Level

---

## SQL Analysis

Example query:

SELECT experience_level, AVG(salary)
FROM gov_jobs
GROUP BY experience_level;

Full queries available in:

sql/analysis.sql

---

## How to Run

1. Run the Python script to fetch and clean data  
2. Generate processed dataset (CSV + SQLite)  
3. Run SQL queries for analysis  

---

## Conclusion

This project demonstrates the ability to:

- Clean and transform real-world data using Python  
- Perform structured analysis using SQL  
- Communicate insights through visualizations  
- Present a complete data analysis workflow  

---

## Author

Freda Choy
