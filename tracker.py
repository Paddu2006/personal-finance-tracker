# Personal Finance Tracker
# By Padma Shree
# Project 3 of 25

import pandas as pd
import matplotlib.pyplot as plt

# Step 1 - Load expenses
df = pd.read_csv(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\01_phase1\finance_tracker\expenses.csv")

# Step 2 - Understand the data
print("=== PERSONAL FINANCE TRACKER ===")
print("Total transactions:", len(df))
print("Total spent: Rs.", df["Amount"].sum())
print("Average spend per transaction: Rs.", round(df["Amount"].mean(), 2))
print("Highest single expense: Rs.", df["Amount"].max())
print("Lowest single expense: Rs.", df["Amount"].min())

# Step 3 - Spending by category
print("\n=== SPENDING BY CATEGORY ===")
category_spend = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
print(category_spend)

# Step 4 - Monthly spending
print("\n=== MONTHLY SPENDING ===")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()
monthly_spend = df.groupby("Month")["Amount"].sum()
print(monthly_spend)

# Step 5 - Charts
# Chart 1 - Spending by category
category_spend.plot(kind="bar", color="purple", figsize=(10,6))
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\01_phase1\finance_tracker\category_spend.png")
plt.show()
print("Chart 1 saved!!")

# Chart 2 - Monthly spending
monthly_spend.plot(kind="bar", color="teal", figsize=(8,5))
plt.title("Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\01_phase1\finance_tracker\monthly_spend.png")
plt.show()
print("Chart 2 saved!!")