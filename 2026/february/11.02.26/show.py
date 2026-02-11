import matplotlib.pyplot as plt
import pandas as pd
from modules.get_file_path import get_path
df= pd.read_csv(get_path(file_name="11.THardwareSales.csv"))
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Total_Sales'] = pd.to_numeric(df['Total_Sales'])
print(df.info())


total_sales = (df.iloc[0:20]).groupby('Region')['Total_Sales'].sum()
region = total_sales.index
print(region)
plt.pie(total_sales, labels=list(region))

#plt.plot(x,y, color="red",marker="*",linestyle="dashdot")
plt.title('Sales over time Graph')
plt.xlabel('Total Sales')
plt.ylabel('Date')
plt.legend()
plt.show()
