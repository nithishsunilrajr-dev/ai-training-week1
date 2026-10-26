import pandas as pd


# Read employee data
df = pd.read_csv("employees.csv")


print("BEFORE CLEANING")
print("Total rows:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())


# Save the original numbers for comparison
before_rows = len(df)
before_missing = df.isnull().sum().sum()
before_duplicates = df.duplicated().sum()


# Remove duplicate records
df = df.drop_duplicates()


# Clean text columns
for col in ["name", "department", "city"]:
    df[col] = df[col].astype("string").str.strip().str.title()


# Fix number columns
df["id"] = pd.to_numeric(df["id"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")


# Fill missing salary with median salary
df["salary"] = df["salary"].fillna(df["salary"].median())


# Fill missing text with the most common value
for col in ["department", "city"]:
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].mode()[0])


# Remove rows without employee ID or name
df = df.dropna(subset=["id", "name"])
df = df[df["name"].str.len() > 0]


# Check salary outliers using IQR
q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3 - q1


lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr


outliers = df[
    (df["salary"] < lower_limit) |
    (df["salary"] > upper_limit)
]


print("\nSalary outliers found:", len(outliers))
# Keep outliers because high salaries may be valid


# Save cleaned data
df.to_csv("clean_data.csv", index=False)


print("\nAFTER CLEANING")
print("Total rows:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())


# Before and after summary
summary = pd.DataFrame({
    "Before": [before_rows, before_missing, before_duplicates],
    "After": [
        len(df),
        df.isnull().sum().sum(),
        df.duplicated().sum()
    ]
}, index=["Rows", "Missing Values", "Duplicates"])


print("\nCLEANING SUMMARY")
print(summary)


print("\nCleaned data saved as clean_data.csv") 