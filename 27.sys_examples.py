#!/usr/bin/env python
# -*- coding: UTF-8 -*-

## This script needs at least two arguments value for correct exectution ##

import sys
## print (sys.stdin.read())

'''
echo 'test_input' | python tutor_examples.py
'test_input'

echo test_somewords | python tutor_examples.py
test_somewords

python tutor_examples.py
abc

^Z
'''

print(sys.maxsize)
print(sys.platform)
print (sys.argv)
print (sys.path)

input_1_File = sys.argv[1]
input_2_File = sys.argv[2]

if len(sys.argv) > 3:
	another_f = sys.argv[3]
	print(another_f)
else:
    print('two arguments.')

for i in sys.modules:
    print('%s  == >   %s' % (i, sys.modules[i]))
