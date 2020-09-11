i = int()
f = 5.0
s = 'rishabh'
b = True

dic = {
    'one': 1,
    'two': 2,
    True: [1,2,3,4,5],
    False: {
        3: 'three',
        4.0: 'four',
        (1,2,4): 'onetwofour'
    }
}

# i = 5.0

lis = [1, 2, 3, 4, 6, 6, 7]
tup = (1, 2, 3, 4, 5, 6, 7)
se = {1, 2, 3, 4, 5, 6, 7}

lis1 = [8, 9, 10]
tup1 = ()
se1 = {}


class Test:
    pass


t = Test()

lis2 = [1, 'one', 1.0, True, {'two': 2}, set(lis), t, [1, 23, 6, 4, (1, 2, 3)]]
# print(lis2)


# for i in lis1:
a = dic[False]
# print(a)
# for k in a:
#     print('key:', k, 'value:', a[k])

lis1 = [1,2,3,4,5]
lis2 = [4,5,6,7,8]
set1 = set(lis1)
set2 = set(lis2)

# print('intersection', set1.intersection(set2))
# print('union', set1.union(set2))
# print(len(set1))
# set1.add(6)
# set2.remove(5)
# print(set1, "\n", set2)

x = 5


def outer():
    global x
    x = 8
    return x ** 2


print(outer())
print(x)
