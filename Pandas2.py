import pandas as pd
data=pd.read_csv('data.csv')
unwanted_values=['?','n.a','Nan']
data.replace(unwanted_values,pd.NA,inplace=True)
data.to_csv('data2.csv',index=False)
print("Dataset cleaned and updated CSV file created successfully.")
data2=pd.read_csv('data2.csv')
print(data2.to_string())