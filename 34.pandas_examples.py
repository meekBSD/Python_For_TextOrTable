

# Lesson 34 - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd
import os

os.chdir('D:/python_lesson/Scripts')

d1 = pd.read_csv('k1.txt', header=None, sep=',')

## output first four rows and first three columns
print(d1.iloc[0:4, 0:3])

## how many columns
print(len(d1.columns))

## how many rows
print(len(d1))

## shape of dataframe , row number and column number
print(d1.shape)

## print data type of each column
for c in d1.columns:
	print(d1[c].dtype)

## change column names
d1.columns = ['item', 'number', 'price', 'category']

## change data type of one column
d1['number'] = d1['number'].astype(float)

# class type of one column
print(type(d1['number']))

## print data type of each column, as we have change dtype of d1['number']
for c in d1.columns:
	print(d1[c].dtype)

## usage of groupby
print(d1.groupby('category')['number'].count())
print(d1.groupby('category').count())

print(d1.groupby('category')['price'].mean())

## select food
print(d1.loc[d1['category'] == 'food'].head(2))

## select food and home appliance by category
c1 = ['food', 'home appliance']
print(d1.loc[d1['category'].isin(c1)])

## select price in a range

print(d1.loc[(d1['price'] >= 5) & (d1['price'] <= 20)])
print(d1.query( '5 <= price <= 20'))

print(d1[(d1['price'] >= 5) & (d1['price'] <= 20)])
print(d1[d1['price'].between(5,20, inclusive=True)])

## plot examples
d1 = pd.read_csv('k1.txt', header=None, sep=',')
d1.columns = ['item', 'number', 'price', 'category']

import matplotlib.pyplot as plt
d1.plot.bar(x='item', y=['price', 'number'])
plt.show()

d1.plot.bar(x='item', y='price')
plt.show()

d1.plot(kind='bar', x='item', y='price', color='orange' )
plt.show()
