"""
copy string contents from a to b. copying from a will charge 1, copying from b will charge 0 (can take a substring)
"""


def string_construction(s):
    charge = 0
    p = ''
    temp = s
    l = len(s)
    while len(p) != l:
        if temp:
            if temp[0] in p:
                p += temp[0]
                temp = temp[1:]
            else:
                p += temp[0]
                temp = temp[1:]
                charge += 1

    return charge


print(string_construction('bccb'))
print(string_construction('abab'))
print(string_construction('abcd'))
