from functools import cmp_to_key


def comparator(x, y):
    if x+y > y+x:
        return -1
    else:
        return 1


def largest_number_from_array(array):
    array = [str(a) for a in array]
    array.sort(key=cmp_to_key(comparator))
    return "".join(array)


def largest_number(array):
    extval, ans = [], ""

    # calculating the length of largest number
    # from given and add 1 for further operation
    l = len(str(max(array))) + 1

    # iterate given values and
    # calculating extended values
    for i in array:
        temp = str(i) * l

        # make tuple of extended value and
        # equivalant original value then
        # append to list
        extval.append((temp[:l:], i))

        # sort extval in descending order
    extval.sort(reverse=True)

    # iterate extended values
    for i in extval:
        ans += str(i[1])

    if int(ans) == 0:
        return "0"
    return ans


print(largest_number([472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412]))
print(largest_number_from_array([472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412]))
