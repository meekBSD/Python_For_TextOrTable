#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("movie_rate.dat", sep = "\t", skiprows=0, header=None)

data.columns = ["movie name", "user_id", "rate_score", "TimeStamp"]
print (data.iloc[1:5, :])
new_data = data.loc[data['movie name']=='Toy Story',]
t_data = new_data.groupby(new_data["rate_score"]).count()["user_id"]

plt.figure(figsize = (8,6), dpi=8)
t_data.plot(kind='barh', color="orange")
plt.savefig('./test1.jpg')

#plt.figure(figsize = (8,6), dpi =8)
#t_data.unstack(level = 0,fill_value=0).plot.bar()
#plt.savefig('./test2.jpg')

plt.figure(figsize=(9,6))
plt.bar(t_data.index , t_data , alpha=0.9, width=0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='one', lw=1)
plt.savefig('./test_bar.jpg')

plt.figure(figsize = (6,6), dpi =8)
labels = ['1 star', '2 stars', '3 stars','4 stars', '5 stars']
plt.pie(t_data, colors=['grey','coral','salmon','yellow','green'], labels = labels)
plt.savefig('./test2.jpg')

#data1 = pd.read_csv("test.tsv.gz",compression= 'gzip', sep='\t', nrows= 10, skiprows=1, header=None)
print(data.groupby("movie name", as_index=False, group_keys=False).mean())


