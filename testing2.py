from itertools import combinations_with_replacement, permutations


def solve(A, B, C):
    A = [str(i) for i in A]
    perm = []
    for i in range(1, B + 1):
        perm += list(combinations_with_replacement(A, i))
        perm += list(permutations(A, i))
    perm = [int(''.join(i)) for i in perm]
    ans = set()
    for i in perm:
        if len(str(i)) == B and i < C:
            ans.add(i)

    # for i in perm:
    # if i < C:
    # ans.add(i)
    return len(ans)


arr = [0,1,2,5]
le = 2
lim = 21
print(solve(arr, le, lim))
