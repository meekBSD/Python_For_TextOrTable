


a = "Test"
b = 10
print("{0}\t{1}".format(a, b))
print("{0}\t{1:.4f}".format(a, b))

print("{0}\t{1:03d}".format(a, b))


print('This is {name}, {age} years old.'.format(name='Rose', age=40))

someone = {'name': 'Rose', 'age': 40, 'job': 'teacher'}
print('I am {person[name]}, {person[age]} years old, a {person[job]}.'.format(person= someone))