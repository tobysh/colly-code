import matplotlib.pyplot as plt
import pandas as pd
from modules.get_file_path import get_path
df= pd.read_csv(get_path(file_name="11.THardwareSales.csv"))
df['DateTime'] = pd.to_datetime(df['DateTime'])
x= df['DateTime']
y = df['Total_Sales']
plt.plot(x,y)
plt.title('Sales over time Graph')
plt.xlabel('Total Sales')
plt.ylabel('Date')
plt.show()
