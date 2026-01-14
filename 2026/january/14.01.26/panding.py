import pandas as pd
from modules.get_file_path import get_path

pharmacy_path = get_path(file_name="10pharmacy.json")
supermarket_path = get_path(file_name="10supermarket.csv")

supermarket = pd.read_csv(supermarket_path)
pharmacy = pd.read_json(pharmacy_path)

print(supermarket.head(12))
print(pharmacy.head(12))
print(pharmacy.shape)
print(pharmacy.info())
print(supermarket.shape)
print(supermarket.info())
print(pharmacy.describe())
print(supermarket.describe())
