from os import rename

import pandas as pd

df =pd.read_csv('orders.csv')
# df =pd.read_csv('orders.csv',header=None)
print(df)
# print(df.head())
# print(df.tail())
# print(df.info())  
# print(df.describe())
# print(df.columns)
# print(df.dtypes)
# print(df.shape)

# df.columns = ['order_date','order_id','ship_date', 'ship_mode', 'customer_key','region', 'product_id', 'category', 'sales', 'quantity', 'profit'] #here we change customer_id to customer_key and changed the position of order_id and order_date 
# print(df)

# rename columns:
# df1 = df.copy()
# df1.rename(columns={'order_id': 'id', 'order_date': 'date'}, inplace=True) 
# print(df1)
# print(df)

# selection columns:

# col = ['order_id', 'order_date','ship_date']
# print(df[col])
# or

# print(df[['order_id', 'order_date','ship_date']])
# df_new = df[['order_id', 'order_date','ship_date']]  assign it new dataframe
# print(df_new)


# print(df.order_date)
# print(type(df))        #daaframe
 
# df_new1 = df['order_date']
# print(type(df_new1))        #series

# select rows and columns:
# print(df.iloc[3:6])  # select rows 3 to 5
# print(df.iloc[3:6, 0:5])  # select rows 3 to 5 and columns at index 0 to 4
# print(df.iloc[[3, 6, 8]])  # select rows 3, 6, and 8
# print(df.iloc[[3, 6, 8], [0, 5]])  # select rows 3, 6, and 8 and columns at index 0 and 5


# print(df.loc[0])  # select first row
# print(df.loc[0:2])  # select first three rows
# print(df.loc[0:2, 'order_id'])  # select first three rows and 'order_id' column
# print(df.loc[0:2, ['order_id', 'order_date']])  # select first three rows and specified columns