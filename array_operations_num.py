import numpy

n, m = map(int, input().split())
# print(n, m)
main = []
for i in range(2):
    a = []
    for j in range(n):
        a.append(list(map(int, input().split()))) 
    main.append(a)

a1 = numpy.array(main[0], int)
a2 = numpy.array(main[1], int)

print(main[0])
print(main[1])

# print(numpy.add(a1, a2))
# print(numpy.subtract(a1, a2))
# print(numpy.multiply(a1, a2))
# # print(numpy.divide(a1, a2))
# print(a1//a2)
# print(numpy.mod(a1, a2))
# print(numpy.power(a1, a2))
