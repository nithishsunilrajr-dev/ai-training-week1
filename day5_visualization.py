import pandas as pd
import matplotlib.pyplot as plt
import os


# Load cleaned employee data
df = pd.read_csv("clean_data.csv")


# Create a folder to save the charts
os.makedirs("reports/figures", exist_ok=True)


# Chart 1 - Average salary by department
avg_salary = df.groupby("department")["salary"].mean()


plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar", color="steelblue")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("reports/figures/1_department_salary.png")
plt.close()


print("Chart 1: Finance has the highest average salary.")


# Chart 2 - Salary distribution
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, color="skyblue", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("reports/figures/2_salary_distribution.png")
plt.close()


print("Chart 2: Salaries vary across the employees.")


# Chart 3 - Employee ID vs Salary
plt.figure(figsize=(8, 5))


for department, group in df.groupby("department"):
    plt.scatter(group["id"], group["salary"], label=department)


plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/3_salary_scatter.png")
plt.close()


print("Chart 3: Employee salaries differ across departments.")


# Chart 4 - Sorted employee salaries
sorted_data = df.sort_values("salary")


plt.figure(figsize=(8, 5))
plt.plot(
    sorted_data["name"],
    sorted_data["salary"],
    marker="o",
    color="steelblue"
)
plt.title("Employee Salaries - Lowest to Highest")
plt.xlabel("Employee")
plt.ylabel("Salary (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/4_salary_line.png")
plt.close()


print("Chart 4: The line shows salaries from lowest to highest.")


# Chart 5 - Salary box plot
plt.figure(figsize=(8, 5))
plt.boxplot(df["salary"])
plt.title("Employee Salary Box Plot")
plt.ylabel("Salary (INR)")
plt.xticks([1], ["Employees"])
plt.tight_layout()
plt.savefig("reports/figures/5_salary_boxplot.png")
plt.close()


print("Chart 5: The box plot shows the spread of salaries.")


print("\nAll five charts saved successfully!")