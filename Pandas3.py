import pandas as pd
data=pd.read_csv('data.csv')
data['price']=pd.to_numeric(data['price'],errors='coerce')
max_price=data.loc[data['price'].idxmax()]
most_expensive_company_name=max_price['company']
most_expensive_price=max_price['price']
print("Most expensive car company name:",most_expensive_company_name)
print("Price of the most expensive car:",most_expensive_price)