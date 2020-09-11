def compare_triplets(a, b):
    alice = bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice +=1
        elif b[i] > a[i]:
            bob += 1
        else:
            pass
    return alice, bob


print(compare_triplets([5, 6, 7], [3, 6, 10]))
