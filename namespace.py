import math
import mymath

print(math.pi)
print(mymath.pi)

x = 1

def f():
    y = x + 1
    print(x)

    def g():
        a = y + 1

    for i in range(10):
        g()
        print(y)
f()