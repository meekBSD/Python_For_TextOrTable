#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import string
letters =string.ascii_uppercase[:8]

f = open('test.txt', 'r')
contents = [i.rstrip() for i in f]
#print(contents)
f.close()

teams = ['Team_' + s for s in letters]
print(teams)

numbers = list(range(12))
new_numbers = [i for i in range(12)]

s_numbers = [ n ** 2 for n in new_numbers]
print(s_numbers)

str_nums = [ str(i) for i in s_numbers]
print('+'.join(str_nums))
print(eval('+'.join(str_nums)))

print(sum(s_numbers))

geometric_prog = [ 3 * (2**n) for n in range(10)]
print(sum(geometric_prog))


