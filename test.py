from os import rename

import pandas as pd

df =pd.read_csv('orders.csv')
# df =pd.read_csv('orders.csv',header=None)
# print(df)
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
# print(type(df))        #dataframe
 
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
# print(df.loc[0:2, ['order_id', 'order_date']])  # select first three rows and specified 

#set index :

# df.set_index('order_id',inplace=True)  # set 'order_id' as the index
# print(df.loc['CA-2020-152156', 'ship_date':'product_id'])
# print(df.loc[['CA-2020-152156', 'CA-2020-138688'],
#              ['ship_date', 'product_id']])
# df.reset_index(inplace=True)  # reset the index to default

# sort_index:
    
# df.sort_index(ascending = False,inplace=True)  # sort the DataFrame by indexprint(fd))
# df.sort_values('sales', ascending = False,inplace=True)  # sort the DataFrame by sales
# df.sort_values(['quantity', 'profit'], ascending = [True,False],inplace=True)  
# df.reset_index(drop=True,inplace=True)  # reset the index to default after sorting(drop ture means we don't want to keep the old index as a column)
# print(df)


# data Filteration:

# df[df['region'] == 'West']
# print(df['region'] == 'West')
# print(df.loc[(df['region'] == 'West') & (df['region'] == 'West'), ['order_id', 'order_date', 'region']])
# print(df[(df['region'] == 'West')])
# print(df[~(df['region'] == 'West')])

df['country']='India'
print(df)
df.drop(columns='country', inplace=True)
print(df)
