def pure(n):
    p = ''
    while n > 0:
        n -= 1

        if n % 2 == 0:
            p += '4'
        else:
            p += '5'

        n = n // 2

    le = len(p)
    p = p[::-1]

    for i in range(le - 1, -1, -1):
        p += p[i]

    return p


for _ in range(int(input())):
    num = int(input())
    print(pure(num))
