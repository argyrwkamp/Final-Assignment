import pandas as pd

df = pd.read_csv('C:\\Users\iro_u\Desktop\datawithin2016_2019.csv')

cn=df.groupby(['zip_code'])['sale_dollars'].max()

df1=df['sale_dollars'].sum()
cn1=df.groupby(['store_number'])['sale_dollars'].sum()/df1 *100



print(cn)
print(cn1)


