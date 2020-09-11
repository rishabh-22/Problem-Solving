input()
a = set(map(int, input().split()))
n = int(input())
su = 0
for _ in range(n):
    op = input().split()[0]
    x = set(map(int, input().split()))
    op = 'a.' + op + '(x)'
    eval(op)
    print(a)
    su += len(a)

print(su)
print(a)
