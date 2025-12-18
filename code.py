import pandas as pd
import os
# create sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [23, 25, 30],
        'City': ['New york', 'Los Angeles', 'Chicago']
        }
df = pd.DataFrame(data)

# Adding new row to df for v2
new_row = {'Name': 'GF1', 'Age': 20, 'City': 'Sedney'}
df.loc[len(df.index)] = new_row

# # Adding new row to df for v2
# new_row2 = {'Name': 'GF2', 'Age': 25, 'City': 'Landon'}
# df.loc[len(df.index)] = new_row2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f'csv file saved to {file_path}')