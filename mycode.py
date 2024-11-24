import pandas as pd
import os

data = {
    "Name" : ["Ali", "Zain", "Kashaf"],
    "Age" : [21, 22, 24],
    "Designation" : ["AI Engineer", "DL Engineer", "UX/UI Designer"]
}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"Sample data saved to {file_path}")