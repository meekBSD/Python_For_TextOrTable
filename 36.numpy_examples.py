#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
np.mean(a, axis=0)
# array([4., 5., 6., 7.])
new_a = a.flatten()
print(new_a)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

b = new_a.reshape(12,1)
np.mean(b, axis=1)
# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.])
np.mean(b, axis=0)
# array([5.5])
np.mean(new_a, axis=0)
# 5.5

print(np.arange(0,100,5))
# [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]


v = [55, 69, 37, 3, 81, 52, 42, 9, 95]
a = np.array(v)
a
# array([55, 69, 37,  3, 81, 52, 42,  9, 95])
print(np.max(a))
# 95
print(np.min(a))
# 3
print(np.median(a))
# 52.0
print(np.mean(a))
# 49.22222222222222
print(np.abs(-1))
# 1
print(np.sin(np.pi/2))
# 1.0
print(np.arctanh(0.462118))
# 0.5000010715784053
print(np.exp(3))
# 20.085536923187668

print(np.power(2,3))
# 8
print(np.sqrt(25))
# 5.0
print(np.dot([1,2], [3,4]))
# 11
print(1 * 3 + 2 * 4)
# 11


# A 和 B 均为一维向量，且均包含有n个元素，则A与B的点积为：
# A[0]*B[0]+A[1]*B[1]+...+A[n]*B[n]

# functions in numpy
# https://www.numpy.org/devdocs/reference/routines.math.html
