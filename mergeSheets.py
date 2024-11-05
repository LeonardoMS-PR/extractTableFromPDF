import pandas as pd

file_path = r'C:\\Users\\leona\\Documents\\contabeis\\demonstrações brf 2020-2024\\bpBrf2019-23.ods'
sheets = pd.read_excel(file_path, engine='odf', sheet_name=None)

# Extract DataFrames
df1 = sheets['ativo']
df2 = sheets['temp_ativo']

# Set the first column as index
df1 = df1.set_index(df1.columns[0])
df2 = df2.set_index(df2.columns[0])

# Align DataFrames by their index (first column)
result = df1.combine_first(df2).reset_index()

print(result)
