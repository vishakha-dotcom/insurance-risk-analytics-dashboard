import pandas as pd
import numpy as np

# CONFIG

NUM_POLICIES = 1000000
VEHICLE_VALUE = 100000


# GENERATE PURCHASE DATES

dates = pd.date_range("2024-01-01", "2024-12-31")

# distribute policies evenly
policies_per_day = NUM_POLICIES // len(dates)

purchase_dates = np.repeat(dates, policies_per_day)

# adjust for remainder
remaining = NUM_POLICIES - len(purchase_dates)
if remaining > 0:
    purchase_dates = np.concatenate(
        [purchase_dates, np.random.choice(dates, remaining)]
    )

np.random.shuffle(purchase_dates)


# GENERATE IDS

customer_id = np.arange(1, NUM_POLICIES + 1)
vehicle_id = np.arange(1, NUM_POLICIES + 1)

# TENURE DISTRIBUTION

tenure_counts = [
    int(NUM_POLICIES * 0.2),
    int(NUM_POLICIES * 0.3),
    int(NUM_POLICIES * 0.4),
    int(NUM_POLICIES * 0.1),
]

tenure = np.concatenate([
    np.full(tenure_counts[0], 1),
    np.full(tenure_counts[1], 2),
    np.full(tenure_counts[2], 3),
    np.full(tenure_counts[3], 4)
])

np.random.shuffle(tenure)


# PREMIUM

premium = tenure * 100


# POLICY DATES

policy_start = pd.to_datetime(purchase_dates) + pd.Timedelta(days=365)
policy_end = policy_start + pd.to_timedelta(tenure * 365, unit="D")


# POLICY DATASET

policy = pd.DataFrame({
    "Customer_ID": customer_id,
    "Vehicle_ID": vehicle_id,
    "Vehicle_Value": VEHICLE_VALUE,
    "Premium": premium,
    "Policy_Purchase_Date": purchase_dates,
    "Policy_Start_Date": policy_start,
    "Policy_End_Date": policy_end,
    "Policy_Tenure": tenure
})

policy.to_csv("policy_sales.csv", index=False)

print("Policy dataset generated")


# CLAIMS 2025

policy["purchase_day"] = policy["Policy_Purchase_Date"].dt.day

claim_days = [7, 14, 21, 28]

eligible = policy[policy["purchase_day"].isin(claim_days)]

claims_2025 = eligible.sample(frac=0.30, random_state=42).copy()

claims_2025["Claim_Date"] = claims_2025["Policy_Start_Date"]
claims_2025["Claim_Amount"] = VEHICLE_VALUE * 0.10
claims_2025["Claim_Type"] = 1

# CLAIMS 2026

four_year = policy[policy["Policy_Tenure"] == 4]

claims_2026 = four_year.sample(frac=0.10, random_state=42).copy()

dates_2026 = pd.date_range("2026-01-01", "2026-02-28")

claims_2026["Claim_Date"] = np.random.choice(dates_2026, len(claims_2026))
claims_2026["Claim_Amount"] = VEHICLE_VALUE * 0.10
claims_2026["Claim_Type"] = 2


# COMBINE CLAIMS

claims = pd.concat([claims_2025, claims_2026], ignore_index=True)

claims["Claim_ID"] = np.arange(1, len(claims) + 1)

claims = claims[[
    "Claim_ID",
    "Customer_ID",
    "Vehicle_ID",
    "Claim_Amount",
    "Claim_Date",
    "Claim_Type"
]]

claims.to_csv("claims_data.csv", index=False)

print("Claims dataset generated")

print("All datasets created successfully")