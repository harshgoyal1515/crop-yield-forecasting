import pandas as pd

# Load datasets
weather_df = pd.read_csv("weather-1.csv")
crop_df = pd.read_csv("Custom_Crops_yield_Historical_Dataset.csv")

# Clean and extract join keys
weather_df.rename(columns={"State/UT": "State", "Last Updated": "Date"}, inplace=True)
weather_df["Date"] = pd.to_datetime(weather_df["Date"], errors="coerce")
weather_df["Year"] = weather_df["Date"].dt.year
weather_df["State"] = weather_df["State"].str.strip().str.lower()
weather_df["District"] = weather_df["District"].str.strip().str.lower()

crop_df.rename(columns={"State Name": "State", "Dist Name": "District"}, inplace=True)
crop_df["State"] = crop_df["State"].str.strip().str.lower()
crop_df["District"] = crop_df["District"].str.strip().str.lower()
crop_df["Year"] = crop_df["Year"].astype("int", errors='ignore')

# Show unique values
print("\n🧪 Weather States:", weather_df["State"].unique()[:10])
print("🧪 Weather Years:", weather_df["Year"].dropna().unique()[:10])
print("🧪 Weather Districts:", weather_df["District"].unique()[:10])

print("\n🌾 Crop States:", crop_df["State"].unique()[:10])
print("🌾 Crop Years:", crop_df["Year"].dropna().unique()[:10])
print("🌾 Crop Districts:", crop_df["District"].unique()[:10])
