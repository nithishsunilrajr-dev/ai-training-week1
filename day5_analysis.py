import pandas as pd


# Load the cleaned employee data
df = pd.read_csv("clean_data.csv")


print("EMPLOYEE DATA ANALYSIS")


# Basic salary statistics
print("\nSalary Statistics")
print(df["salary"].agg(["mean", "median", "min", "max", "std"]))


# Compare departments
print("\nDepartment Salary Comparison")
department_summary = df.groupby("department").agg(
    employees=("id", "count"),
    average_salary=("salary", "mean"),
    total_salary=("salary", "sum")
)
print(department_summary)


# Compare cities
print("\nCity Salary Comparison")
city_summary = df.groupby("city").agg(
    employees=("id", "count"),
    average_salary=("salary", "mean")
)
print(city_summary)


# Find correlations
print("\nCorrelations")
numeric_data = df.select_dtypes(include="number")
correlations = numeric_data.corr()
print(correlations)


# Show the strongest available relationships
pairs = correlations.where(
    ~pd.DataFrame(
        [[i == j for j in correlations.columns]
         for i in correlations.index],
        index=correlations.index,
        columns=correlations.columns
    )
).stack().reset_index()


pairs.columns = ["Column 1", "Column 2", "Correlation"]
pairs["pair"] = pairs.apply(
    lambda row: tuple(sorted([row["Column 1"], row["Column 2"]])),
    axis=1
)
pairs = pairs.drop_duplicates("pair")
pairs = pairs.sort_values(
    "Correlation", key=abs, ascending=False
)


print("\nTop Correlations")
print(pairs[["Column 1", "Column 2", "Correlation"]].head(3))


# Five business questions
print("\nBUSINESS QUESTIONS")


print("\n1. How many employees are there?")
print(len(df))


print("\n2. What is the average salary?")
print(round(df["salary"].mean(), 2))


print("\n3. Which department has the highest average salary?")
print(department_summary["average_salary"].idxmax())


print("\n4. Which city has the most employees?")
print(df["city"].value_counts().idxmax())


print("\n5. What is the highest salary?")
print(df["salary"].max())


# Merge with department budget data
budget = pd.DataFrame({
    "department": ["Sales", "Hr", "It", "Finance"],
    "budget": [100000, 120000, 250000, 150000]
})


merged_data = pd.merge(
    department_summary.reset_index(),
    budget,
    on="department",
    how="left"
)


print("\nDepartment Budget Comparison")
print(merged_data)


# Bonus: Pivot table
print("\nDepartment and City Pivot Table")
pivot = pd.pivot_table(
    df,
    values="salary",
    index="department",
    columns="city",
    aggfunc="mean"
)
print(pivot)


print("\nAnalysis completed!")