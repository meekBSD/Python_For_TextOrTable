#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = u'大家好，我在练习python.'
for s in a :
    print(s)

# - - - - - - -  - - - - -  - - - - - - -

MyList = [1,2,3,4,1,2,3,1,2,1,5]
for ele in MyList:
    print(ele)

# - - - - - - -  - - - - -  - - - - - - -

for i in range(0,11):
    print(i)

# - - - - - - -  - - - - -  - - - - - - -

test_List = ['A', 12, "XYZ"]
for i in test_List:
    if isinstance(i, str):
        print('%s is a string.' % i)

    elif isinstance(i, int):
        print('%d is a integer number.' % i)

# - - - - - - -  - - - - -  - - - - - - -
	
x = [12, 19, 'not a number', 9, 1, 3, 17]
for i in x:
    if isinstance(i, str):
        print('%s is a string.' % i)
    elif isinstance(i, int) and i > 5:
        print('find a number larger than 5: %d .' % i)
	
