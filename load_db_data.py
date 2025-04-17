import pandas as pd
import sqlite3
from icecream import ic


file_path = "data.xls"
df = pd.read_excel(file_path)
ic(df)

annual = df.groupby('API WELL  NUMBER')[['OIL', 'GAS', 'BRINE']].sum().reset_index()
ic(annual)

conn = sqlite3.connect("production_data.sqlite3")
annual.to_sql("annual_production", conn, if_exists="replace", index=False)

print("DB load Done")
