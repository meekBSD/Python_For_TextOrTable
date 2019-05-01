#!/usr/bin/python
# -*- coding: UTF-8 -*-

# - - - - - - - - - - - - - - - - - - - - - - - - -

import os
import glob
# import sys

## check the current directory and change directory, then check file type ##

print (os.getcwd())

os.chdir('D:/python_lesson/Scripts')
print(os.path.exists('one_src_file.txt'))

for f in os.listdir('.'):
    absolute_path_name =  os.sep.join(['D:/python_lesson/Scripts', f])
    if os.path.isdir(absolute_path_name):
        print(absolute_path_name)

#sys.exit()

src_file = 'path_test.py'
if os.path.exists(src_file) and not os.path.exists('renamed_file.py'):
	os.rename(src_file, 'renamed_file.py')

test_StringIO_files = []                   ## define a list
python_scripts = glob.glob('*.py')
for i in python_scripts:

    fsize = os.path.getsize(i)
    fsize = fsize/float(1024)
    print('the file size of %s is %f K' %(i, fsize))
    file_handle = open(i, 'r')
    file_contents = file_handle.read()
    if file_contents.find('import StringIO') != -1:
        test_StringIO_files.append(i)                   # add file name to the 'test_StringIO_files' List

    file_handle.close()
print ('%d python code files have "import StringIO" module' % (len(test_StringIO_files)))


walk_paths = os.walk('D:/python_lesson', topdown=True)
for root, dirs, files in walk_paths:
    print('root dir : %s' % (root))
    print('directories in root are : %s' % (dirs))
    print('files are : %s' % (files))
                        
