stones = [2, 7, 4, 1, 8, 1]

while len(stones) > 1:
    max1 = max(stones)
    stones.remove(max1)
    max2 = max(stones)
    stones.remove(max2)
    if max1 - max2 > 0:
        stones.append(max1 - max2)

if len(stones):
    print(stones[0])
else:
    print(0)
