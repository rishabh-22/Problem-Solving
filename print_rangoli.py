# import string
# alpha = string.ascii_lowercase
#
# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))


def print_formatted(number):
    # your code goes here
    # w = len("{0:b}".format(number))
    # for i in range(1, number+1):

    #     print(i, "{0:o} {0:x} {0:b}".format(i, width=w))
    # n = 17
    w = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
