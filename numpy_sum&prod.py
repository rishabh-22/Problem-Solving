import numpy

r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(map(int, input().split())))

print(arr)
arr = numpy.array(arr)
summ = numpy.sum(arr, axis=0)
print(summ)
print(numpy.prod(summ))

