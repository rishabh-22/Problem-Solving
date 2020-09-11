def viral_advertising(n):
    total = [2]
    likes_today = 2
    for i in range(1, n):
        shares_today = likes_today * 3
        likes_today = shares_today // 2
        total.append(likes_today)
    return sum(total)


print(viral_advertising(5))
