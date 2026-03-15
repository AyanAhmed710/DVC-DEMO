import pandas as pd
import os

data = {"Name" : ["Ali" , "Qasim" , "labeed"],
        "Age" : [2,3,4],
        "place" : ["Lahore" , "Karachi" , "Faislabad"]}

new_row={"Name" : "Alice" ,"Age" :3 , "place" : "Turkey"}

df=pd.DataFrame(data)

df.loc[len(df.index)] = new_row

data_dir = "data"

os.makedirs(data_dir ,exist_ok=True)

file_path = os.path.join(data_dir , "data.csv")

df.to_csv(file_path ,index=False)

print(file_path)

