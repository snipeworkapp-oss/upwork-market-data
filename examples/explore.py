# Example: load and explore the Upwork Market Index dataset
#
#   pip install pandas matplotlib
#   python explore.py

import pandas as pd

BASE = "https://raw.githubusercontent.com/snipeworkapp-oss/upwork-market-data/main/data"

weekly = pd.read_csv(f"{BASE}/weekly.csv")
categories = pd.read_csv(f"{BASE}/categories.csv")
countries = pd.read_csv(f"{BASE}/countries.csv")

print("=== Latest week ===")
print(weekly.tail(1).T)

print("\n=== Highest-paying categories by hourly rate (latest week) ===")
latest = categories["week"].max()
top = (categories[categories["week"] == latest]
       .sort_values("avg_hourly_usd", ascending=False)
       [["category", "avg_hourly_usd", "avg_fixed_usd", "jobs"]])
print(top.to_string(index=False))

print("\n=== Fixed vs hourly split over time ===")
print(weekly[["week", "fixed_share", "hourly_share"]].to_string(index=False))

# Uncomment to plot:
# import matplotlib.pyplot as plt
# weekly.plot(x="week", y="avg_fixed_usd", marker="o",
#             title="Upwork average fixed budget by week")
# plt.tight_layout(); plt.savefig("avg_fixed_trend.png", dpi=120)
# print("saved avg_fixed_trend.png")
