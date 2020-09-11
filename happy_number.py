def is_happy(n: int) -> bool:
    c = 1
    while c < 20:
        s = 0
        for i in str(n):
            s = s + int(i) ** 2
        if s == 1:
            return True
        c += 1
        n = s
    else:
        return False


print(is_happy(19))
