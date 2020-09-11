import numpy

r = int(input())
arr = []

for j in range(2):
    temp = []
    for i in range(r):
        temp.append(list(map(int, input().split())))
    arr.append(temp)

# print(arr)

a, b = arr[0], arr[1]

# print(a, "\n", b)
a = numpy.array(a)
b = numpy.array(b)

print(numpy.dot(a, b))
