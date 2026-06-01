
from os import rename


from click import group
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

# add new column:
# df['country']='India'
# print(df)
# df.drop(columns='country', inplace=True)    #drop column
# df.drop(index=[0,1,2], inplace=True)          #drop row
# print(df)


# df['price_flag'] = 1
# print(df['price_flag'].dtypes)            # check datatype of price_flag column
# print(df['price_flag'].astype('int64'))   # change datatype of price_flag column

# print(df)
# df.loc[df['profit'] < 0, 'price_flag'] = 0
# print(df)

# df['price_type'] = 'High'
# df.loc[(df['profit'] >= 0) & (df['profit'] <= 50), 'price_type'] = 'Medium'
# df.loc[df['profit'] < 0, 'price_type'] = 'Loss'
# print(df)


# using apply function:

# df['category_count']= df['category'].apply(len)
# df['category_upper']= df['category'].apply(str.upper)
# df['category_lower']= df['category'].apply(str.lower)

# print(df)
# df.drop(columns=['category_count','category_upper','category_lower'], inplace=True)
# print(df)

# def profit_loss(profit):
#     if profit < 0:
#         return 'Loss'
#     else:
#         return 'Profit'
    
# df['profit_loss'] = df['profit'].apply(profit_loss)
# print(df)


# print(df.isnull())    # check for null values
# print(df.isnull().sum())  # count of null values in each column
# df.info()   #quick summary of the DataFrame, including the number of non-null values and data types of each column

# df.dropna(inplace=True)    # drop all rows with null values
# df.dropna(subset=['sales'],inplace=True)  # drop all rows with null values in the 'sales' column
# print(df)


# df.fillna("Unknown",inplace=True)                     # fill all null values with "Unknown"
# df['category'].fillna("Unknown",inplace=True)         # fill all null values with "Unknown" for 'category' column
# df['sales'].fillna(df['sales'].mean(), inplace=True)  # fill null values in 'sales' column with the mean of the column
# df.fillna(method='ffill', inplace=True)               # forward  fill null values
# df.fillna(method='bfill', inplace=True)               # backward fill null values

# data = {
#     "Name": [
#         "Alice", "Bob", "Charlie", "Alice",
#         "David", "Bob", "Eve", "Frank",
#         "Eve", "George"
#     ],
#     "Age": [25, 30, 35, 25, 40, 30, 28, 33, 28, 45]
# }

# df = pd.DataFrame(data)
# print(df)

# df.drop_duplicates(keep ='last',inplace=True)   # drop last duplicate index rows
# df.drop_duplicates(keep ='first',inplace=True)  # drop first duplicate index rows
# df.drop_duplicates(subset=['Age','Name'],keep ='last',inplace=True) # drop duplicate rows based on 'Age' column
# print(df)


# date and time:
# print(df)


df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y', errors='coerce')  
df['ship_date']  = pd.to_datetime(df['ship_date'], format='%d-%m-%Y', errors='coerce')
# convert 'order_date' column to datetime format
# print(df['order_date'])  # check datatype of 'order_date' column
# print(df['order_date'].dt.year)   # extract year from 'order_date' column
# print(df['order_date'].dt.month)  # extract month from 'order_date' column
# print(df['order_date'].dt.day)    # extract day from 'order_date' column


# print(df[df['order_date'] >= '2021-01-01'])
# df['transit_time'] = (df['ship_date'] - df['order_date']).dt.days  # calculate transit time in days
# print(df)

#agregation:

# df['region'].unique()  # get unique values in 'region' column
# print(df['region'].unique())
# df['category'].unique()  
# print(df['category'].unique())



# df.groupby('category')['sales'].sum()  # group by 'category' and calculate total sales for each category
# print(df.groupby('category')['sales'].sum())
# print(df.groupby('category')['sales'].count())  # group by 'category' and count the number of sales for each region

# print(df.groupby('category')['sales'].agg(['sum', 'mean', 'max', 'min']))  # group by 'category' and calculate total, average, maximum, and minimum sales for each region
# print(df.groupby('category').agg({
#     'sales': 'sum',
#     'profit': 'mean'
# }))  # group by 'category' and calculate total sales and average profit for each category
                                           
# print(df['category'].value_counts(dropna=False))  # count the number of occurrences of each category, including NaN values

# print(df.pivot_table(index='region', columns='category', values='sales', aggfunc='sum', fill_value=0))  # create a pivot table to summarize sales by region and category
df_oreders =  pd.read_csv('orders.csv')
df_returns =  pd.read_csv('returns.csv')
# print(df_returns)
df1 = pd.merge(left=df_oreders, right=df_returns, on='order_id', how='inner') 
print(df1)  # print the merged DataFrame
