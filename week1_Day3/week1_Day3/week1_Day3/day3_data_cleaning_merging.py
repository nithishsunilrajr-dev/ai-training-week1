import pandas as pd

# Step 1: Load the orders CSV file
orders = pd.read_csv("orders.csv")

print("Original orders:")
print(orders)

# Step 2: Count missing values
print("\nMissing values:")
print(orders.isna().sum())

# Step 3: Count duplicate rows
print("\nDuplicate rows:")
print(orders.duplicated())

print("Number of duplicates:", orders.duplicated().sum())

# Step 4: Remove duplicate rows
orders = orders.drop_duplicates()

# Step 5: Convert amount to a numeric data type
orders["amount"] = pd.to_numeric(orders["amount"])

# Step 6: Find the median of available amounts
median_amount = orders["amount"].median()
print("\nMedian used:", median_amount)

# Step 7: Fill missing amounts with the median
orders["amount"] = orders["amount"].fillna(median_amount)

# Step 8: Convert order_id to string
orders["order_id"] = orders["order_id"].astype(str)

print("\nCleaned orders:")
print(orders)

# Step 9: Group orders by customer
customer_summary = orders.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print("\nCustomer summary:")
print(customer_summary)
# Step 10: Load customer details
customers = pd.read_csv("customers.csv")

print("\nCustomer details:")
print(customers)

# Step 11: Inner join
inner_join = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)

print("\nInner join:")
print(inner_join)
print("Inner join rows:", len(inner_join))

# Step 12: Left join
left_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left",
    indicator=True
)

# Find customers who have no matching order
no_orders = left_join.loc[
    left_join["_merge"] == "left_only",
    "name"
]

print("\nCustomers with no orders:")
print(", ".join(no_orders))

# Step 13: Outer join
outer_join = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="outer",
    indicator=True
)

# Find orders whose customer record is missing
orders_without_customer = outer_join.loc[
    outer_join["_merge"] == "left_only",
    ["order_id", "customer_id"]
]

print("\nOrders without customer records:")
print(orders_without_customer)
# Bonus: Combine two monthly order datasets

january_orders = pd.DataFrame({
    "customer_id": [101, 102],
    "amount": [500, 600]
})

february_orders = pd.DataFrame({
    "customer_id": [101, 103],
    "amount": [700, 300]
})

# Combine both months row by row
monthly_orders = pd.concat(
    [january_orders, february_orders],
    ignore_index=True
)

print("\nCombined monthly orders:")
print(monthly_orders)

# Calculate total amount and number of orders per customer
monthly_summary = monthly_orders.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("amount", "count")
)

print("\nMonthly customer summary:")
print(monthly_summary)
