# 🚕 Yellow Taxi Trip Data Analysis (January 2022)

This project involves cleaning and analyzing **New York Yellow Taxi Trip Data (Jan 2022)**. The original data was provided in **Parquet format** and visualized using **Power BI** to extract insights on transportation behavior, fare distribution, and passenger metrics.

---

## 📁 Dataset Overview

- **Source**: NYC Yellow Taxi Trip Records
- **File**: `yellow_tripdata_2022-01.parquet`
- **Total Records**: ~2.4 million trips

---

## 🔧 Data Cleaning Process (using Python & Pandas)

Before visualizing, the data had **inconsistencies and missing values**, which were resolved through a systematic cleaning process.

### 🔴 Major Data Issues Found

| Column Name             | Issue Type                     | Fix Applied                              |
|------------------------|-------------------------------|-------------------------------------------|
| `airport_fee`          | Negative values, nulls        | Replaced -1.25 with 1.25, nulls with 0.0  |
| `congestion_surcharge` | Negative values, nulls        | Replaced -2.5 with 2.5, nulls with mean 2.3 |
| `store_and_fwd_flag`   | Missing values                | Filled all nulls with `'N'`               |
| `RatecodeID`           | Nulls, invalid value `99.0`   | Filled nulls with 1, replaced 99 with 1   |
| `passenger_count`      | Nulls                         | Filled all nulls with default 1           |

All columns were checked for:
- Missing values (`NaN`)
- Invalid or impossible values (e.g., negative fare/fee)
- Incorrect or unmapped codes

### ✅ Final Result After Cleaning
✔ No missing or negative values  
✔ Ratecode and Payment codes properly labeled  
✔ Data transformed and exported for visualization

---

## 📊 Power BI Dashboard

The cleaned dataset was used to create an **interactive Power BI dashboard**, highlighting key insights from taxi operations.

### 🎨 Visualizations Created

| Visualization | Description |
|---------------|-------------|
| 📌 **Ratecode Summary (Pie Chart)** | Shows distribution of fare types like Standard, JFK, Newark, etc. |
| 💰 **Fare Components (Donut Chart)** | Shows fare breakdown: tips, tolls, airport fee, congestion surcharge |
| 📍 **Trip Distance by Month (Line Chart)** | Highlights monthly trip distances |
| 📦 **Top Pickup vs Drop-off Locations (Bar Chart)** | Compares PULocationID vs DOLocationID |
| 👤 **Passenger Count (Bar Chart)** | Total passenger volume |
| 💳 **Payment Method (Pie Chart)** | Labeled pie chart showing Credit, Cash, Dispute, etc. |

---

## 📌 Insights Derived

- **Standard Rate** trips are the most common (~96% of rides)
- Majority of passengers **paid via Credit Card**
- Most trips occurred in January and December
- **Passenger count peaks** in specific zones (Pickup & Drop-off)
- **Airport fee and congestion surcharge** contribute a notable share of fare total

---
## 🖼 Dashboard Preview

![Power BI Dashboard Preview](project.png)


## 🛠 Tools & Technologies Used

- **Python**: Data cleaning with `pandas` and `numpy`
- **Power BI**: Interactive dashboard creation
- **Jupyter Notebook / VS Code**: Coding environment
- **GitHub**: Code and report hosting

---

## 📁 Files in this Repo

| File Name | Description |
|-----------|-------------|
| `cleaned_yellow_tripdata.csv` | Final cleaned dataset |
| `powerbi_dashboard.png`       | Snapshot of Power BI visuals |
| `project_cleaning_script.py` | Python cleaning script |
| `README.md`                   | This documentation file |

---

## 🙌 Author

👨‍💻 **Mohammad Ashfaq Ur Rahman**  
🎓 B.Tech CSE, SBIT College  
📍 Khammam, India

---

## 📢 Final Note

This project showcases **real-world data cleaning + business intelligence reporting**.  
It’s perfect for a **data analyst portfolio** and demonstrates proficiency in handling messy data, understanding trends, and presenting results clearly.

Feel free to ⭐️ the repo if you found it helpful!
