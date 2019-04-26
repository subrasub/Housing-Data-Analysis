import pandas as pd

mlb_file_path = './melb_data.csv'
mlb_data = pd.read_csv(mlb_file_path)
mlb_data.describe()