import numpy
import matplotlib.pyplot as plt


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
masx = []
masy = []
for i in range(1, n):
    masx.append(fibonacci(i))
    masy.append(i)
plt.plot(masx, masy)
plt.show()
