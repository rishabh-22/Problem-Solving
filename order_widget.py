def filled_orders(order, k):
    # Write your code here
    w = k
    total = 0
    while len(order) > 0 and min(order) <= w:
        o = min(order)
        order.remove(o)
        w -= o
        total += 1
    return total


print(filled_orders([10, 30], 40))
