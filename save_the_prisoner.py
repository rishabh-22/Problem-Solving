def saveThePrisoner(n, m, s):
    end_sweets = m % n
    # if end_sweets == 0:
    #     return n
    if end_sweets == 1:
        return s
    else:
        final = (s + end_sweets - 1) % n
        if final == 0:
            return n
        else:
            return final


# for i in range(int(input())):
    # n, m, s = map(int, input().split())
print(saveThePrisoner(499999999, 999999997, 2))
