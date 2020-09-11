"""
given an array of numbers, find the possible numbers in it which are powers of two.
"""


def power_of_two(n):
    x = int(n) if n[0] != '0' else 0
    return x and (not(x & (x - 1)))


def two_two(a):
    sub_strings = []
    i = 0
    while i < len(a):
        for l in range(1, len(a)+1-i):
            sub_strings.append(a[i:i+l])
        i += 1

    count = 0
    for p in sub_strings:
        if power_of_two(p):
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        a = input()
        result = two_two(a)
        print(result)
