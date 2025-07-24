import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clean_crop_weather_historical.csv")

# Define features and target with corrected column names
features = ['JUN', 'JUL', 'AUG', 'SEP', 'RICE AREA (1000 ha)']
target = 'RICE YIELD (Kg per ha)'

# Drop rows with missing values in relevant columns
df = df.dropna(subset=features + [target])

# Split into features and target
X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score: {r2:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")

# Plot predictions
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, alpha=0.6, color='teal')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # y=x line
plt.xlabel("Actual Rice Yield (Kg/ha)")
plt.ylabel("Predicted Rice Yield (Kg/ha)")
plt.title("Actual vs Predicted Rice Yield")
plt.grid(True)
plt.tight_layout()
plt.savefig("rice_yield_prediction.png")
plt.show()
