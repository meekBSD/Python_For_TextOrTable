#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# Lesson 28 - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import math

test_file = "k1.txt"
f_process = open(test_file , 'r')

things  = []
price   = []
number  = []
thing_category = []

for line in f_process:
    line_splits = line.rstrip().split(',')
    things.append(line_splits[0])
    number.append(int(line_splits[1]))
    price.append(float(line_splits[2]))
	
    thing_category.append(line_splits[3])

f_process.close()
prices_list = []
tot_price = 0
for n, i in enumerate(price):
    single_price = price[n] * number[n]
    prices_list.append(single_price)

print(math.fsum(prices_list))

# Lesson 29 - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from collections import defaultdict

item_d = defaultdict(list)
f_process = open(test_file , 'r')
for line in f_process:
    line_splits = line.rstrip().split(',')
    thing = line_splits[0]
    item_d[thing].append(int(line_splits[1]))
    item_d[thing].append(float(line_splits[2]))	
    item_d[thing].append(line_splits[3])

f_process.close()

prices_list = []
for i in item_d:
    prices_list.append(item_d[i][0] * item_d[i][1])

print(math.fsum(prices_list))

from collections import Counter

MyList = [1,2,3,4,1,2,3,1,2,1,5]
ListCount = Counter(MyList)
print(ListCount)

for e in ListCount.items():
    print('Item: ', e[0], 'Appears', e[1], 'times.')

categoryCount = Counter(thing_category)
print(categoryCount.most_common())

least_common = reversed(categoryCount.most_common())
print(list(least_common))

# Lesson 30 - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from collections import namedtuple
What = namedtuple('Item', 'the_name,number,price,the_category')
list_item = []

f_process = open(test_file , 'r')
for line in f_process:
    line_splits = line.rstrip().split(',')
    t = What(the_name= line_splits[0], number=int(line_splits[1]), price=float(line_splits[2]), the_category=line_splits[3])
    list_item.append(t)
f_process.close()


print(list_item)
for i in list_item:
    print(i.the_name, i.number, i.price, i.the_category)

from collections import OrderedDict

dic = OrderedDict()
f_process = open(test_file , 'r')
for line in f_process:
    line_splits = line.rstrip().split(',')
    dic[line_splits[0]] = '\t'.join(line_splits[1:])
f_process.close()

print(dic)
dic.move_to_end('bread')
print(dic)

## dic.pop('pears')
## dic.popitem()
