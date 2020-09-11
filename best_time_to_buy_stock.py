prices = [7, 1, 5, 3, 6, 4]

diff = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        diff += prices[i] - prices[i - 1]
print(diff)
