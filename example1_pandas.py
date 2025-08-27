import pandas as pd

# Example dataset (normally you'd load from CSV/Excel/Database)
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03", "2025-01-03"],
    "Product": ["Laptop", "Laptop", "Mouse", "Laptop", "Mouse"],
    "Price": [1200, 1150, 25, 1190, 30],
    "Quantity": [1, 2, 5, 1, 10]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Add a new column: Total sales
df["Total_Sales"] = df["Price"] * df["Quantity"]

# Preview dataset
print("=== Raw Data ===")
print(df)

# Basic descriptive statistics
print("\n=== Statistics ===")
print(df.describe())

# Group by Product: total revenue
print("\n=== Revenue per Product ===")
print(df.groupby("Product")["Total_Sales"].sum())

# Daily total sales
print("\n=== Daily Sales ===")
print(df.groupby("Date")["Total_Sales"].sum())

# Find the best-selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
print(f"\nBest-selling product: {best_product}")
