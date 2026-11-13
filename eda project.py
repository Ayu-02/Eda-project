
import pandas as pd
import numpy as np

# =====================================
# STEP 1: LOAD DATASET
# =====================================

df = pd.read_excel(
    r"C:\Users\HP\Downloads\datasets_eda.xlsx"
)

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)


# =====================================
# STEP 2: DATASET INFORMATION
# =====================================

print("\nDataset Information:")
df.info()

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())


# =====================================
# STEP 3: REMOVE DUPLICATES
# =====================================

duplicate_count = df.duplicated().sum()

df = df.drop_duplicates()

print("\nDuplicates Removed:", duplicate_count)


# =====================================
# STEP 4: CLEAN COLUMN NAMES
# =====================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Columns:")
print(df.columns.tolist())


# =====================================
# STEP 5: CLEAN TEXT DATA
# =====================================

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()


# =====================================
# STEP 6: FILL MISSING VALUES USING fillna()
# =====================================

# Count missing coupon values before filling
missing_coupon_before = df["couponcode"].isnull().sum()

# Fill missing coupon codes
df.fillna({
    "couponcode": "No Coupon"
}, inplace=True)

print("\nCoupon Codes Filled:", missing_coupon_before)


# Fill missing numerical values with median
numeric_columns = [
    "quantity",
    "itemsincart",
    "unitprice",
    "totalprice"
]

for col in numeric_columns:
    if col in df.columns and df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

# Check missing values after filling
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# =====================================
# STEP 7: CONVERT DATA TYPES
# =====================================

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
).astype("Int64")

df["itemsincart"] = pd.to_numeric(
    df["itemsincart"],
    errors="coerce"
).astype("Int64")

df["unitprice"] = pd.to_numeric(
    df["unitprice"],
    errors="coerce"
)

df["totalprice"] = pd.to_numeric(
    df["totalprice"],
    errors="coerce"
)


# =====================================
# STEP 8: IDENTIFY INVALID RECORDS
# =====================================

invalid_mask = (
    (df["quantity"] <= 0) |
    (df["unitprice"] <= 0) |
    (df["itemsincart"] <= 0) |
    (df["totalprice"] < 0) |
    (df["date"].isna())
)

invalid_records = df[invalid_mask].copy()

print("\nInvalid Records:")
print(invalid_records)


# =====================================
# STEP 9: CHECK PRICE CALCULATIONS
# =====================================

df["expected_total"] = (
    df["quantity"] * df["unitprice"]
)

price_mismatch = ~np.isclose(
    df["totalprice"].astype(float),
    df["expected_total"].astype(float),
    atol=0.01,
    equal_nan=False
)

print("\nIncorrect Price Calculations:")
print(df[price_mismatch])


# =====================================
# STEP 10: CREATE CLEANING REPORT
# =====================================

report = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Duplicate Rows Removed",
        "Missing Coupon Codes Filled",
        "Invalid Records",
        "Price Mismatches",
        "Remaining Missing Values"
    ],

    "Value": [
        len(df),
        len(df.columns) - 1,
        duplicate_count,
        missing_coupon_before,
        len(invalid_records),
        int(price_mismatch.sum()),
        int(
            df.drop(columns=["expected_total"])
            .isnull().sum().sum()
        )
    ]
})


# =====================================
# STEP 11: REMOVE TEMPORARY COLUMN
# =====================================

df.drop(
    columns=["expected_total"],
    inplace=True
)


# =====================================
# STEP 12: EXPORT CLEANED DATASET
# =====================================

with pd.ExcelWriter(
    "cleaned_dataset.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Cleaned_Data",
        index=False
    )

    report.to_excel(
        writer,
        sheet_name="Cleaning_Report",
        index=False
    )


# =====================================
# STEP 13: FINAL OUTPUT
# =====================================

print("\n================================")
print("DATA CLEANING COMPLETED!")
print("================================")

print("\nFinal Dataset Shape:", df.shape)

print("\nCleaning Report:")
print(report)

print("\nFile saved: cleaned_dataset.xlsx")
# Display first 10 rows of cleaned dataset
print("\nFirst 10 Rows of Cleaned Dataset:")
print(df.head(10))
print(df.info())