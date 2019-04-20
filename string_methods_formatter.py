#!/usr/bin/env python
# -*- coding: UTF-8 -*-


>>> Shape = 'Rectangle'

>>> Shape.find('tangle')
3
>>> Shape.index('ang')        ## when the substring exists in primary string, it will return substring's index, if not , raise error
4
>>> len(Shape)
9
>>> Shape.replace('Rect','Tri')
'Triangle'

>>> print("The shape is %s" % Shape)
The shape is Rectangle

>>> print("The shape is %+12s" % Shape)
The shape is    Rectangle
>>> print("The shape is %s" % Shape.rjust(12,'*'))
The shape is ***Rectangle
>>> print("The shape is %s" % Shape.rjust(12,'*').ljust(15,'*'))
The shape is ***Rectangle***

>>> Width = 5
>>> print("The width of %s is %d" % (Shape, Width))
The width of Rectangle is 5
>>> print("The room No. is %04d" % (23))
The room No. is 0023
>>> print("The shape is %r" % Shape)
The shape is 'Rectangle'


>>> a = [1,10,15,25]
>>> print("The List is %s" % a)
The List is [1, 10, 15, 25]

