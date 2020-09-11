from collections import OrderedDict

grocery = OrderedDict()
n = int(input())
for i in range(n):
    key, price = '', ''
    data = input()
    for char in data:
        if char.isdigit():
            price += char
        else:
            key += char

    if key in grocery.keys():
        grocery[key] += int(price)
    else:
        grocery[key] = (int(price))

# print(grocery)
grocery = dict(grocery)
for k, v in grocery.items():
    print(k[:-1], v)
