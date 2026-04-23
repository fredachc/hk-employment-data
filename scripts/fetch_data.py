from datetime import datetime
import requests
import json
from pathlib import Path
import pandas as pd
import re
import sqlite3

# ✅ 英文版本
URL = "https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json"

# ✅ 用 script 位置做基準，避免路徑亂掉
BASE_DIR = Path(__file__).resolve().parent.parent
today_str = datetime.today().strftime("%Y-%m-%d")
output_path = BASE_DIR / "data" / "raw" / f"jobs_raw_{today_str}.json"
output_path.parent.mkdir(parents=True, exist_ok=True)


def extract_salary(s):
    if pd.isna(s):
        return None

    s = str(s).strip()

    if s == "":
        return None

    matches = re.findall(r'[\d,]+', s)

    if matches:
        numbers = []
        for x in matches:
            try:
                numbers.append(int(x.replace(",", "")))
            except:
                continue

        if numbers:
            return max(numbers)

    return None


def map_experience_level(x):
    if pd.isna(x):
        return None
    if x <= 2:
        return "Entry"
    elif x <= 5:
        return "Mid"
    else:
        return "Senior"


def map_salary_level(x):
    if pd.isna(x):
        return None
    if x >= 60000:
        return "High"
    else:
        return "Low"


try:
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    # ✅ 解決 BOM 問題
    text = response.content.decode("utf-8-sig")
    data = json.loads(text)

    # 💾 存 raw data
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ 成功下載 raw data")
    print(f"📁 儲存位置: {output_path.resolve()}")

    # 查看最外層資料結構
    if isinstance(data, dict):
        print("📦 最外層: dict")
        print("🔑 keys:", list(data.keys())[:10])
    elif isinstance(data, list):
        print("📦 最外層: list")
        print("📊 筆數:", len(data))
        if len(data) > 0:
            print("🔑 第一筆 keys:", list(data[0].keys()))
    else:
        print("⚠️ 未知結構:", type(data))

    # ✅ 抽真正 records
    records = data["common"][0]["vacancies"]

    print("\n📊 records 筆數:", len(records))
    print("🔑 第一筆 keys:", list(records[0].keys()))

    # ✅ 轉 DataFrame
    df = pd.DataFrame(records)

    print("\n📄 DataFrame 預覽:")
    print(df.head())

    print("\n📌 欄位:")
    print(df.columns)

    # ✅ 揀重要欄位
    df_selected = df[[
        "jobname",
        "deptnamejve",
        "entrypay",
        "enddate",
        "expfrom",
        "expto"
    ]].copy()

    print("\n🎯 精簡資料:")
    print(df_selected.head())

    # ✅ 清洗 salary
    df_selected["salary"] = df_selected["entrypay"].apply(extract_salary)

    print("\n🔍 salary 檢查:")
    print(df_selected[["entrypay", "salary"]].head(10))

    # ✅ 篩選月薪
    df_selected["is_monthly"] = df_selected["entrypay"].str.contains("month", case=False, na=False)

    df_monthly = df_selected[df_selected["is_monthly"] == True].copy()

    print("\n📊 只保留月薪:")
    print(df_monthly[["entrypay", "salary"]].head())

    # ✅ 轉日期（保留作展示用途）
    df_monthly["enddate"] = pd.to_datetime(df_monthly["enddate"], errors="coerce")

    print("\n📅 日期檢查:")
    print(df_monthly[["jobname", "enddate"]].head(10))

    # ✅ 建立經驗層級
    df_monthly["experience_level"] = df_monthly["expfrom"].apply(map_experience_level)

    # ✅ 建立高薪 / 低薪分類
    df_monthly["salary_level"] = df_monthly["salary"].apply(map_salary_level)

    print("\n🧠 經驗層級檢查:")
    print(df_monthly[["expfrom", "experience_level"]].head(10))

    print("\n💼 高薪 / 低薪檢查:")
    print(df_monthly[["salary", "salary_level"]].head(10))

    # ✅ 基本統計
    print("\n💰 平均月薪：", round(df_monthly["salary"].mean(), 2))
    print("💰 最高月薪：", df_monthly["salary"].max())
    print("💰 最低月薪：", df_monthly["salary"].min())

    print("\n🏢 招聘最多部門：")
    print(df_monthly["deptnamejve"].value_counts().head(5))

    # ✅ 匯出 CSV（給 Excel 用）
    processed_dir = BASE_DIR / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    csv_path = processed_dir / "jobs_cleaned.csv"
    df_monthly.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"\n📁 已輸出 CSV: {csv_path}")

    # ✅ 寫入 SQLite database（給 SQL 用）
    db_path = processed_dir / "job_analysis.db"

    conn = sqlite3.connect(db_path)
    df_monthly.to_sql("gov_jobs", conn, if_exists="replace", index=False)
    conn.close()

    print(f"✅ SQLite database 已建立: {db_path}")

except Exception as e:
    print("❌ 錯誤:", e)