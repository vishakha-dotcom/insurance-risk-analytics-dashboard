
# Insurance Risk Analytics Dashboard

## Overview
This project simulates and analyzes an insurance portfolio to study premium revenue, claim patterns, and portfolio risk. 
A dataset of **1,000,000 insurance policies** was generated using Python and analyzed using SQL. 
The results were visualized using **Power BI** to better understand claim trends and profitability.

The objective of this project was to practice **data simulation, SQL analysis, and dashboard visualization** using a real-world business scenario.

---

## Problem Statement
An insurance company wants to analyze historical policy sales and claim activity to understand profitability and risk exposure.

To simulate this scenario:

- 1,000,000 policies were generated for the year 2024
- Policies have tenures of **1, 2, 3, or 4 years**
- Claims occur under specific conditions in **2025 and early 2026**

The analysis focuses on answering questions related to:

- Total premium collected
- Claim costs and claim trends
- Claim-to-premium ratios
- Future claim liabilities
- Overall portfolio loss ratio

---

## Tools & Technologies

- **Python (Pandas, NumPy)** – dataset simulation
- **SQL (SQLite)** – analytical queries
- **Power BI** – dashboard visualization

---

## Dataset Description

### Policy Sales Data

Fields included:

- Customer_ID  
- Vehicle_ID  
- Vehicle_Value (₹100,000)  
- Premium (₹100 per year of policy tenure)  
- Policy_Purchase_Date  
- Policy_Start_Date  
- Policy_End_Date  
- Policy_Tenure  

Policy tenure distribution:

| Tenure | Percentage |
|------|------|
| 1 Year | 20% |
| 2 Years | 30% |
| 3 Years | 40% |
| 4 Years | 10% |

Policies start **365 days after purchase date**.

---

### Claims Data

Claims were simulated using the following rules:

- In **2025**, vehicles purchased on the **7th, 14th, 21st, and 28th** of each month have a **30% probability of filing a claim**
- Claim amount = **10% of vehicle value (₹10,000)**
- Between **January 1 – February 28, 2026**, **10% of vehicles with 4‑year policies file a second claim**

---

## Key Metrics Calculated

The analysis includes:

- Total Premium Collected
- Monthly Claim Cost
- Claim Cost to Premium Ratio
- Claim Ratio by Policy Tenure
- Potential Future Claim Liability
- Portfolio Loss Ratio

---

## Key Results

| Metric | Value |
|------|------|
| Total Premium Collected | ₹240M |
| Total Claims | ~₹493M |
| Portfolio Loss Ratio | ~2.06 |
| Potential Future Claim Liability | ~₹9.5B |

### Insights

- **3-year policies show the most balanced risk profile**
- Claims increase in **early 2026 due to second claims from long-tenure policies**
- Under current assumptions, the simulated portfolio appears **loss-making**

---

## Dashboard

A **Power BI dashboard** was created to visualize the results.

The dashboard includes:

- Monthly claim cost trend
- Claims vs premium by policy tenure
- Policy tenure distribution
- Total claim cost by year

---

## Project Structure

```
insurance-risk-analytics-dashboard
│
├── data
│   ├── policy_sales.csv
│   ├── claims_data.csv
│   └── monthly_claims.csv
│
├── scripts
│   ├── dataset_generator.py
│   └── analysis_sql.py
│
├── dashboard
│   └── Insurance_Risk_Dashboard.pbix
│
├── report
│   └── Insurance_Policy_Risk_Profitability_Report.docx
│
└── README.md
```

---

## What I Learned

Through this project I gained experience with:

- Generating large synthetic datasets
- Writing SQL queries for business analysis
- Interpreting claim patterns and risk exposure
- Building dashboards for business insights

---

## Future Improvements

Possible extensions for this project:

- Predicting claim probability using machine learning
- Simulating additional insurance products
- Automating the data pipeline
- Deploying the dashboard with live data updates
