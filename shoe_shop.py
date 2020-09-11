from collections import Counter
z = input()
shoe_list = list(map(int, input().split()))
shoe_dict = dict(Counter(shoe_list))
# print(shoe_dict)

sale = 0

for i in range(int(input())):
    size, money = map(int, input().split())
    # print(i, size, money)
    try:
        if shoe_dict[size] > 0:
            sale += money
            shoe_dict[size] -= 1
    except KeyError:
        pass

print(sale)
