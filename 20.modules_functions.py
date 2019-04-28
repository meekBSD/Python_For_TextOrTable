# - - - - - - - - - - - - - - - - - - - - - - - - -

import distutils
modules = distutils.sys.modules
standard_libs = []
for i in modules:
    mod_desc = str(modules[i])
    if mod_desc.find(r'C:\\Program Files (x86)\\Python3\\lib') != -1:
        standard_libs.append(i)

print(len(standard_libs))

import sys
print(sys.path)

import pip
third_party = pip.get_installed_distributions()
print(len(third_party))

from datetime import datetime
a = datetime.now()
print(a.strftime('%Y/%m/%d %H:%M:%S'))

## if error happens , use 'pip install numpy' to install numpy module.
import numpy as np
print(np.std([1 , 2 , 3, 4 , 5], ddof = 1 ))

import statistics
print(statistics.stdev([1 ,2, 3, 4, 5]))

import itertools

res1 = list(itertools.permutations(['A', 'B', 'C', 'D'] , 3))
print(res1)

res2 = list(itertools.combinations('XYZUVW', 2))
print(res2)
