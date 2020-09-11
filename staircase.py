# make a staircase using #, pattern building.


def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end="")
        print('#' * i)


staircase(6)
