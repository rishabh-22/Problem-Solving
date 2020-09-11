"""
find the number of occurrences of a substring in a string.
"""


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag = 1
            for j in range(0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag = 0
                    break
            if flag == 1:
                count += 1
    print(count)
    return count


count_substring("XNFOEGHUNOAEFGHUFQIWEGHU", 'GHU')
