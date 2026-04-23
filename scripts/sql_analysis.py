import sqlite3
from pathlib import Path
import pandas as pd

# 設定路徑
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "data" / "processed" / "job_analysis.db"

# 連接 SQLite database
conn = sqlite3.connect(db_path)

queries = {
    "1_overall_avg_salary": """
        SELECT ROUND(AVG(salary), 2) AS avg_salary
        FROM gov_jobs;
    """,

    "2_salary_range": """
        SELECT 
            MAX(salary) AS max_salary,
            MIN(salary) AS min_salary
        FROM gov_jobs;
    """,

    "3_top_10_departments_by_avg_salary": """
        SELECT 
            deptnamejve,
            ROUND(AVG(salary), 2) AS avg_salary
        FROM gov_jobs
        GROUP BY deptnamejve
        ORDER BY avg_salary DESC
        LIMIT 10;
    """,

    "4_avg_salary_by_experience_level": """
        SELECT 
            experience_level,
            ROUND(AVG(salary), 2) AS avg_salary
        FROM gov_jobs
        GROUP BY experience_level
        ORDER BY avg_salary DESC;
    """,

    "5_job_count_by_experience_level": """
        SELECT 
            experience_level,
            COUNT(*) AS job_count
        FROM gov_jobs
        GROUP BY experience_level
        ORDER BY job_count DESC;
    """,

    "6_salary_level_distribution": """
        SELECT 
            salary_level,
            COUNT(*) AS job_count
        FROM gov_jobs
        GROUP BY salary_level
        ORDER BY job_count DESC;
    """,

    "7_experience_level_vs_salary_level": """
        SELECT
            experience_level,
            salary_level,
            COUNT(*) AS job_count
        FROM gov_jobs
        GROUP BY experience_level, salary_level
        ORDER BY experience_level, salary_level;
    """,

    "8_top_5_departments_by_job_count": """
        SELECT
            deptnamejve,
            COUNT(*) AS job_count
        FROM gov_jobs
        GROUP BY deptnamejve
        ORDER BY job_count DESC
        LIMIT 5;
    """
}

print(f"✅ Connected to database: {db_path}")

for name, query in queries.items():
    print(f"\n{'='*60}")
    print(f"{name}")
    print(f"{'='*60}")

    df_result = pd.read_sql_query(query, conn)
    print(df_result)

conn.close()
print("\n✅ All SQL queries completed.")