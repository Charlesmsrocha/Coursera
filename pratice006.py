product = 1
for n in range(1,10):
    product = product * n

print(product)

#######################################################

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result + i
    return result

print(factorial(4))
print(factorial(5))

########################################################

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))


