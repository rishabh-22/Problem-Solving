# n = input()
# arr = list(map(lambda x: True if int(x) > 0 else False, input().rstrip().split()))
# # arr2 = list(map(lambda x: True if x > 0 else False, arr))
# arr.append(True if len(n) == 1 else (True if n[0] == n[1] else False))
# print(arr)
# print(all(arr))

N, n = int(input()), input().split()
print("N: ", N, "\n", "n: ", n)
a = any([j == j[::-1] for j in n])
print("a: ", a)
b = [j == j[::-1] for j in n]
print("b: ", b)
print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))
