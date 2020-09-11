cube = lambda x: x**3


def fibonacci(n):
    n1, n2 = 0, 1
    final = []
    count = 0
    while count < n:
        final.append(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return final


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))