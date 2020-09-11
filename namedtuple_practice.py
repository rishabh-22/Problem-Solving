from collections import namedtuple

lis = []
n = int(input())
data = namedtuple('Student', input())
for i in range(n):
    z = input().split()
    x = data(*z)
    # print(x)
    lis.append(x)
# print(lis)

marks = []
for element in lis:
    marks.append(int(element.MARKS))

print("%.2f" % (sum(marks)/n))

# "5 \nMARKS CLASS NAME ID\n92 2 Calum 1\n82 5 Scott 2\n94 2 Jason 3\n55 8 Glenn 4\n82 2 Fergus 5"
