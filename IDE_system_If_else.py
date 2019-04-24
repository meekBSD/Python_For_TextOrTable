#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

system_info = sys.platform
if system_info.startswith('win'):
    print('We can use Spyder, PyCharm or Rodeo.')
elif system_info.startswith('linux'):
    print('Maybe we can use Vim/Vi.')
else:
    print('Maybe we can use Xcode or Vi.')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
answer = 2 * 3 * 4 * 5 * 6

print('Please calculate the result of " 2 * 3 * 4 * 5 * 6" ')
user_Answer = eval(input('Please input your answer: '))
if user_Answer == answer:
    print('You are right.')
else:
    print('Wrong.')
