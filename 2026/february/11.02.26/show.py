import matplotlib.pyplot as plt
import pandas as pd
from modules.get_file_path import get_path
df= pd.read_csv(get_path(file_name="11.THardwareSales.csv"))
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Total_Sales'] = pd.to_numeric(df['Total_Sales'])

plt.hist(df['Total_Sales'], bins=10, color='purple')
plt.title('Distribution of Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['Units_Sold'], bins=5, color='lime')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.show()

traffic = pd.read_json(get_path(file_name="traffic_data.json"))
vehicle_count = (df.iloc[0:100]).groupby('location')['vehicle_count'].sum()
location = vehicle_count.index
plt.bar(location, vehicle_count, color='lime')
plt.title('Traffic by location')
plt.xlabel('Location')
plt.ylabel('Vehicle count')
plt.show()