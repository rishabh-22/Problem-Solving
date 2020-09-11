arr = list(map(int, input().rstrip().split()))
total = []
for i in range(arr[1]):
    total.append(list(map(float, input().rstrip().split())))

# arr2 = list(map(float, input().rstrip().split()))
# arr3 = list(map(float, input().rstrip().split()))

main = zip(*total)
final = []
# print(arr1, arr2, arr3)
for element in main:
    final.append(sum(element)/arr[1])

# print(final)
for i in final:
    print("%.2f" %i)
