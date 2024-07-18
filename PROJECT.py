import pandas as pd
import sqlalchemy as sq
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
print(df.head(5))

df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
print(df)

df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")

df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)

engine = sq.create_engine('mssql://sa:12345@localhost\SQLEXPRESS/Project2saylani?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()

df.to_sql('df_orders', con=conn , index=False, if_exists = 'replace')