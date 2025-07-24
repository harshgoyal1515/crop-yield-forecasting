import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("clean_crop_weather_historical.csv")

# Select columns with 'YIELD' in their name
yield_cols = [col for col in df.columns if 'YIELD' in col.upper()]

# Build a DataFrame of average yields
avg_yields = {}
for col in yield_cols:
    crop = col.replace(" YIELD (Kg per ha)", "").strip().title()
    avg = df[col].mean(skipna=True)
    avg_yields[crop] = avg

# Convert to DataFrame
yield_df = pd.DataFrame(list(avg_yields.items()), columns=["Crop", "Average Yield (kg/ha)"])
yield_df = yield_df.sort_values(by="Average Yield (kg/ha)", ascending=False)

# Plot
plt.figure(figsize=(12, 6))
plt.bar(yield_df["Crop"], yield_df["Average Yield (kg/ha)"], color='mediumseagreen')
plt.xticks(rotation=75, ha='right')
plt.title("Average Crop Yields Across All Years")
plt.xlabel("Crop")
plt.ylabel("Average Yield (kg/ha)")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("average_crop_yields.png", dpi=300)


plt.show()
