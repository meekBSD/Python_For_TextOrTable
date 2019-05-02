
import random
for i in range(10):
    print(random.randint(1,20))

print(random.choice( ['apple', 'pear', 'peach', 'orange', 'lemon']))

print(random.sample(list(range(30)),10))     

rand_List = [random.choice(list(range(30))) for i in range(50)]
print(rand_List)

items = [1,2,3,4,5,6]
random.shuffle(items)
print(items)

items = [1,2,3,4,5,6]
random.seed(1)
random.shuffle(items)
print(items)
