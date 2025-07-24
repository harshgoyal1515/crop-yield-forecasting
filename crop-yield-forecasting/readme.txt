# 🌾 Intelligent Crop Yield Forecasting Using Big Data Analytics

This project uses historical crop production and weather data to perform exploratory data analysis, Spark-based distributed processing, and machine learning-based prediction of crop yield.

## 📁 Structure
- `data/`: Cleaned CSV datasets
- `scripts/`: Python scripts for EDA, Spark, and ML modeling
- `notebooks/`: Jupyter notebooks for analysis and testing
- `outputs/`: Generated plots
- `docs/`: Report and Presentation
- `environment.yml`: Conda environment file

## ⚙️ How to Run
```bash
conda env create -f environment.yml
conda activate crop-forecast
python scripts/eda_historical.py
python scripts/spark_analysis.py
python scripts/ml_prediction.py
