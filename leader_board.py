import copy


def climbing_leader_board(scores, alice):
    ans = []
    for score in alice:
        mock = copy.copy(scores)
        mock.append(score)
        a = set(mock)
        mock = list(a)
        mock.sort(reverse=True)
        b = mock.index(score)
        ans.append(b+1)
    return ans


scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
print(climbing_leader_board(scores, alice))


# faster solution. check how it works.
"""
def climbingLeaderboard(scores,alice):
    arr = []
    l = 0
    p = -1
    for i in scores:
        if p!=i:
            l+=1
        arr.append((l,i))
        p = i
    l = len(alice)
    p = len(scores)-1
    index =0
    
    while p>=0:
        i,j = arr[p]
        if index ==l: break
        s = alice[index]
        if s <= j:
            yield i if s==j else i+1
            index+=1
            continue
        p-=1
    else:
        for _ in range(l-index):
            yield 1
input()
scores = list(map(int,input().split()))
input()
alice = list(map(int,input().split()))

print(*climbingLeaderboard(scores,alice),sep="\n")
"""