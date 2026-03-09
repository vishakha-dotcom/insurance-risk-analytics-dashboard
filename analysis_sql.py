import pandas as pd
import sqlite3

# start analysis and confirm script is running
print("Starting analysis...")

# read generated CSV datasets
policy = pd.read_csv("policy_sales.csv")
claims = pd.read_csv("claims_data.csv")

# convert date columns to datetime
policy["Policy_Purchase_Date"] = pd.to_datetime(policy["Policy_Purchase_Date"])
claims["Claim_Date"] = pd.to_datetime(claims["Claim_Date"])

# print dataset sizes for verification
print("Policy rows:", len(policy))
print("Claims rows:", len(claims))

# create in-memory SQLite database
conn = sqlite3.connect(":memory:")

# load datasets as SQL tables
policy.to_sql("policy_sales", conn, index=False, if_exists="replace")
claims.to_sql("claims", conn, index=False, if_exists="replace")

print("Tables loaded successfully")


# calculate total premium collected
query1 = """
SELECT SUM(Premium) AS total_premium
FROM policy_sales
"""

print("\nTotal Premium Collected:")
print(pd.read_sql(query1, conn))


# calculate monthly claim cost
query2 = """
SELECT
strftime('%Y', Claim_Date) AS year,
strftime('%m', Claim_Date) AS month,
SUM(Claim_Amount) AS total_claim_cost
FROM claims
GROUP BY year, month
ORDER BY year, month
"""

monthly_claims = pd.read_sql(query2, conn)

print("\nMonthly Claim Cost:")
print(monthly_claims)

# export monthly claims for visualization
monthly_claims.to_csv("monthly_claims.csv", index=False)


# calculate claim ratio by policy tenure
query3 = """
SELECT
p.Policy_Tenure,
SUM(c.Claim_Amount)*1.0 / SUM(p.Premium) AS claim_ratio
FROM policy_sales p
LEFT JOIN claims c
ON p.Customer_ID = c.Customer_ID
GROUP BY p.Policy_Tenure
"""

print("\nClaim Ratio by Tenure:")
print(pd.read_sql(query3, conn))


# calculate claim ratio by policy purchase month
query4 = """
SELECT
strftime('%m', p.Policy_Purchase_Date) AS sale_month,
SUM(c.Claim_Amount)*1.0 / SUM(p.Premium) AS claim_ratio
FROM policy_sales p
LEFT JOIN claims c
ON p.Customer_ID = c.Customer_ID
GROUP BY sale_month
ORDER BY sale_month
"""

print("\nClaim Ratio by Sales Month:")
print(pd.read_sql(query4, conn))


# estimate potential future claim liability
query5 = """
SELECT
(COUNT(*) - COUNT(c.Customer_ID)) * 10000 AS potential_liability
FROM policy_sales p
LEFT JOIN claims c
ON p.Customer_ID = c.Customer_ID
"""

print("\nPotential Future Claim Liability:")
print(pd.read_sql(query5, conn))

print("\nAnalysis completed successfully")