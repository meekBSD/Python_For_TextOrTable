


# Lesson 35 - - - - - - - - - - - - - - - - - - - - - - - - -

import string
print(len(string.printable))

print(string.digits)

print(string.hexdigits)

print(string.octdigits)

print(dir(string))
print(string.ascii_lowercase)
print(string.ascii_uppercase)


import string
file_object = 'species.txt'
infile = open( file_object , 'r')
for line_num, line in enumerate(infile):
    lr = line.rstrip()
    for i in lr:
        if i not in string.printable:
            #print('%s\t%d\t%s' %(i.encode("cp936"), line_num,lr[:20]))
            print('%s\t%d\t%s' %(repr(i), line_num,lr[:20]))
            break
infile.close()

