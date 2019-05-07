
def Say_hello():
    print ("Hello!")

Say_hello()
Say_hello()


def Greeting(someone):

    words = 'How are you, ' + someone + ' ?'   
    return words

print(Greeting(u'小兰'))

def add(x, y):
    return x + y

x = add(9, 10)
print(x)

# 求阶乘

def test_factorial(n):

    results = 1

    for i in range(1, n+1):
        results *= i
    return results

print(test_factorial(6))
