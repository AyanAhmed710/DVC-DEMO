import pandas as pd
import os

data = {"Name" : ["Ali" , "Qasim" , "labeed"],
        "Age" : [2,3,4],
        "place" : ["Lahore" , "Karachi" , "Faislabad"]}

df=pd.DataFrame(data)

data_dir = "data"

os.makedirs(data_dir ,exist_ok=True)

file_path = os.path.join(data_dir , "data.csv")

df.to_csv(file_path ,index=False)

print(file_path)

