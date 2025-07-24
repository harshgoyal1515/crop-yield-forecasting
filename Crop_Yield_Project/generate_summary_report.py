import pandas as pd
import re

# Load dataset
df = pd.read_csv("clean_crop_weather_historical.csv")

# Extract relevant columns
area_columns = [col for col in df.columns if "AREA" in col.upper()]
yield_columns = [col for col in df.columns if "YIELD" in col.upper()]

def extract_crop(col_name):
    return re.sub(r" AREA.*| YIELD.*", "", col_name).strip().lower()

# Match crop pairs
crops = []
for area_col in area_columns:
    crop_base = extract_crop(area_col)
    for yield_col in yield_columns:
        if extract_crop(yield_col) == crop_base:
            crops.append((crop_base.title(), area_col, yield_col))
            break

# Create summary
report = []
for crop_name, area_col, yield_col in crops:
    try:
        avg_area = pd.to_numeric(df[area_col], errors='coerce').mean()
        avg_yield = pd.to_numeric(df[yield_col], errors='coerce').mean()
        if pd.notnull(avg_area) and pd.notnull(avg_yield):
            report.append({
                "Crop": crop_name,
                "Average Area (1000 ha)": round(avg_area, 2),
                "Average Yield (kg/ha)": round(avg_yield, 2)
            })
    except Exception as e:
        print(f"❌ Skipping {crop_name} due to error: {e}")

# Save if report is non-empty
if report:
    summary_df = pd.DataFrame(report)
    summary_df.to_csv("crop_yield_summary_report.csv", index=False)
    print("✅ Report saved as crop_yield_summary_report.csv")
else:
    print("⚠️ No data available to generate report.")

