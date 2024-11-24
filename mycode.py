import pandas as pd
import os

data = {
    "Name" : ["Ali", "Zain", "Kashaf"],
    "Age" : [21, 22, 24],
    "Designation" : ["AI Engineer", "DL Engineer", "UX/UI Designer"]
}

df = pd.DataFrame(data)

# adding new row in data for V2
new_row = {'Name': 'Muneeb', 'Age': 25, 'Designation': 'Flutter Developer'}
df.loc[len(df.index)] = new_row

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"Sample data saved to {file_path}")