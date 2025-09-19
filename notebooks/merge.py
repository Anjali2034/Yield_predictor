# import pandas as pd

# # Load the merged dataset
# merged_path = r"C:\Users\anjal\OneDrive\Desktop\merged_dataset_fixed.csv"
# merged = pd.read_csv(merged_path)

# print("✅ Loaded merged dataset:", merged.shape)

# # 1. Backfill missing 'production' values
# missing_prod_before = merged['production'].isna().sum()
# merged['production'] = merged['production'].fillna(merged['yield'] * merged['area'])
# missing_prod_after = merged['production'].isna().sum()
# print(f"🔧 Missing 'production' before: {missing_prod_before}, after fix: {missing_prod_after}")

# # 2. Drop rows with missing 'crop'
# missing_crop_before = merged['crop'].isna().sum()
# merged = merged.dropna(subset=['crop'])
# missing_crop_after = merged['crop'].isna().sum()
# print(f"🔧 Missing 'crop' before: {missing_crop_before}, after fix: {missing_crop_after}")

# # 3. Check if any other missing values remain
# missing_summary = merged.isna().sum()
# print("\n🔍 Remaining missing values per column (top 20):")
# print(missing_summary.sort_values(ascending=False).head(20))

# # 4. Save cleaned dataset
# clean_path = r"C:\Users\anjal\OneDrive\Desktop\merged_dataset_clean.csv"
# merged.to_csv(clean_path, index=False)
# print(f"\n✅ Cleaned dataset saved to: {clean_path}")


import pandas as pd

# Load the cleaned dataset
clean_path = r"C:\Users\anjal\OneDrive\Desktop\merged_dataset_clean.csv"
df = pd.read_csv(clean_path)

print("✅ Loaded cleaned dataset:", df.shape)

# 1. Check missing values per column
missing_values = df.isna().sum()
print("\n🔍 Missing values per column:")
print(missing_values[missing_values > 0] if missing_values.any() else "No missing values!")

# 2. Check missing value percentage
missing_percent = (df.isna().sum() / len(df)) * 100
print("\n🔍 Missing value percentage (top 20):")
print(missing_percent.sort_values(ascending=False).head(20))

# 3. Check for duplicates (optional but good for ML)
duplicates = df.duplicated().sum()
print(f"\n🔍 Duplicate rows: {duplicates}")

# 4. Check numeric columns for proper types
numeric_cols = df.select_dtypes(include='number').columns
print("\n🔍 Numeric columns types:")
print(df[numeric_cols].dtypes)

# 5. Quick data sanity check: min/max of numeric columns
print("\n🔍 Numeric column ranges:")
print(df[numeric_cols].agg(['min', 'max']))

















   





