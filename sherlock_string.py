from collections import Counter


def is_valid(s):
    d = dict(Counter(s))
    values_list = list(d.values())
    values_set = set(values_list)
    print(values_list)
    print(values_set)
    flag = True
    if len(values_set) > 2:
        return 'NO'
    if len(values_set) == 1:
        return 'YES'
    else:
        for i in values_set:
            if values_list.count(i) > 1:
                flag = False
            else:
                flag = True
        if flag:
            return 'YES'
        else:
            return 'NO'


print(is_valid('aabbccddee'))
