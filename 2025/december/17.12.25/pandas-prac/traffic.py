from modules.get_file_path import get_path
import pandas as pd

file_path = get_path("assets","traffic_data.json")

traffic_df = pd.read_json(file_path)

print(traffic_df.info())

data = get_path("assets","pandas_data_1.csv")

pandata = pd.read_csv(data)

new_pandata = pandata.dropna()

pandata.dropna(subset=['Calories'])

pandata.fillna({"Calories":130})

x = pandata["Calories"].mean()

new_new_pandata = pandata.fillna({"Calories":pandata["Calories"].mean()})

print(new_new_pandata.info())

duration = pandata["Duration"]
multi_duration = pandata[["Duration", "Calories"]]