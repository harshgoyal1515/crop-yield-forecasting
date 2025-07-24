import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean
df = pd.read_csv("clean_crop_weather_historical.csv")
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
    .str.replace("/", "_")
)

# Create output directory
import os
os.makedirs("plots", exist_ok=True)

# 1️⃣ Plot: Yield distribution for major crops
yield_cols = [col for col in df.columns if col.endswith("_yield_kg_per_ha")]

for col in yield_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col].dropna(), bins=10, kde=True, color="skyblue")
    plt.title(f"Distribution of {col.replace('_yield_kg_per_ha','').replace('_',' ').title()} Yield")
    plt.xlabel("Yield (kg/ha)")
    plt.tight_layout()
    plt.savefig(f"plots/{col}_distribution.png")
    plt.close()

# 2️⃣ Correlation between all crop yields
plt.figure(figsize=(12, 8))
sns.heatmap(df[yield_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("📊 Correlation Between Crop Yields")
plt.tight_layout()
plt.savefig("plots/crop_yield_correlation_heatmap.png")
plt.close()

# 3️⃣ Rainfall vs Selected Crop Yield (e.g., rice)
if "rice_yield_kg_per_ha" in df.columns and "jun" in df.columns:
    df["avg_monsoon"] = df[["jun", "jul", "aug", "sep"]].mean(axis=1)

    plt.figure(figsize=(7, 5))
    sns.scatterplot(x="avg_monsoon", y="rice_yield_kg_per_ha", data=df)
    plt.title("🌧️ Avg Monsoon Rainfall vs Rice Yield")
    plt.xlabel("Avg Rainfall (Jun–Sep)")
    plt.ylabel("Rice Yield (kg/ha)")
    plt.tight_layout()
    plt.savefig("plots/rice_yield_vs_rainfall.png")
    plt.close()
