import time

b = 7

def verdubbelB(b):
    return b + b

b = verdubbelB(b)
print(b)

# print(time.strftime(("%H:%M:%S)))
print(time.strftime("%H:%M:%S"))

# def f(y):
#   return 2*y + 1
# print(f(3)+g(3))
# def g(x)
#   return 5 + x + 10

def f(y):
    return 2 * y + 1

def g(x):
    return 5 + x + 10

print(f(3) + g(3))