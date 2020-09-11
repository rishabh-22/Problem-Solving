from itertools import permutations

word, n = input().split()

perm = permutations(word, int(n))
perm = ["".join(x) for x in perm]
perm.sort()
for i in perm:
    print(i)
