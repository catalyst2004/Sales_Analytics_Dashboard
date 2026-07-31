import pandas as pd

# Load dataset
df = pd.read_csv("data/walmart.csv")

# -----------------------------
# 1. Display basic information
# -----------------------------
print(df.info())
print(df.head())

# -----------------------------
# 2. Check missing values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 3. Remove duplicate rows
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# 4. Convert date columns
# -----------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# -----------------------------
# 5. Remove leading/trailing spaces
# -----------------------------
text_columns = df.select_dtypes(include=["object", "string"]).columns
df[text_columns] = df[text_columns].apply(lambda col: col.str.strip())

# -----------------------------
# 6. Check data types
# -----------------------------
print("\nData Types:")
print(df.dtypes)

# -----------------------------
# 7. Check unique values
# -----------------------------
for col in text_columns:
    print(f"\n{col}")
    print(df[col].nunique())

# -----------------------------
# 8. Statistical summary
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# 9. Save cleaned dataset
# -----------------------------
df.to_csv("data/walmart_cleaned.csv", index=False)

print("\nData cleaning completed successfully!")