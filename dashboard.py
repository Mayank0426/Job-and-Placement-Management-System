import csv
import os
import matplotlib.pyplot as plt
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))

def read_csv(filename):
    with open(os.path.join(BASE, filename), newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))

students = read_csv("students.csv")
jobs = read_csv("jobs.csv")
applications = read_csv("applications.csv")

print("\n===== PLACEMENT DASHBOARD =====")
print("Total Students:", len(students))
print("Total Jobs:", len(jobs))
print("Total Applications:", len(applications))
print("Selected Applications:", sum(1 for a in applications if a["status"] == "Selected"))

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
branches = Counter(s["branch"] for s in students)
if branches:
    axes[0, 0].bar(branches.keys(), branches.values())
axes[0, 0].set_title("Students by Branch")
axes[0, 0].set_ylabel("Students")

cgpa = [float(s["cgpa"]) for s in students if s.get("cgpa")]
if cgpa:
    axes[0, 1].hist(cgpa, bins=5, edgecolor="black")
axes[0, 1].set_title("CGPA Distribution")
axes[0, 1].set_xlabel("CGPA")

statuses = Counter(a["status"] for a in applications)
if statuses:
    axes[1, 0].bar(statuses.keys(), statuses.values())
axes[1, 0].set_title("Applications by Status")
axes[1, 0].tick_params(axis="x", rotation=20)

if jobs:
    axes[1, 1].bar([j["company"] for j in jobs], [float(j["package"]) for j in jobs])
axes[1, 1].set_title("Company Packages")
axes[1, 1].set_ylabel("Package (LPA)")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(BASE, "dashboard.png"), dpi=150, bbox_inches="tight")
print("Dashboard saved as dashboard.png")
plt.show()
