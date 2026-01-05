import pandas as pd

supermarket = pd.read_csv(r"supermarket.csv")
pharmacy = pd.read_json(r"pharmacy.json")
print(f"Supermarket: {supermarket.head(12)}")
print(f"Pharmacy: {pharmacy.head(12)}")

print(f"Supermarket shape: {supermarket.shape}")
print(f"Pharmacy shape: {pharmacy.shape}")

print(f"Supermarket Info: {supermarket.info()}")
print(f"Pharmacy Info: {pharmacy.info()}")

print(f"Supermarket Description: {supermarket.describe()}")
print(f"Pharmacy Description: {pharmacy.describe()}")

outputs = f"---Supermarket---\n{supermarket.head(12)}\n---Pharmacy---\n{pharmacy.head(12)}\n---Supermarket Shape---\n{supermarket.shape}\n---Pharmacy Shape---\n{pharmacy.shape}\n---Supermarket Info---\n{supermarket.info()}\n---Pharmacy Info---\n{pharmacy.info()}\n---Supermarket Description---\n{supermarket.describe()}\n---Pharmacy Description---\n{pharmacy.describe()}"
with open("outputs.txt", "w") as file:
    file.write(outputs)