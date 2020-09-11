from datetime import datetime


def flatland_space_stations(n, c):
    # ans = []
    # for i in range(n):
    #     dist = []
    #     for s in c:
    #         dist.append(abs(s-i))
    #     ans.append(min(dist))
    # return max(ans)
    maxx = 0
    i1, i2 = 0, 0
    for i in range(len(c)):
        if abs(c[i] - c[i-1]) > maxx:
            maxx = abs(c[i] - c[i-1])
            i1 = i
            i2 = i+2
    # return (maxx+1)//2
    ans = []
    for i in range(n):
        dist = []
        for s in range(i1, i2):
            dist.append(abs(c[s]-i))
        ans.append(min(dist))
    return max(ans)


n, _ = map(int, input().split())
lis = list(map(int, input().split()))
start = datetime.now()
print(flatland_space_stations(n, lis))
end = datetime.now()
print(end-start)