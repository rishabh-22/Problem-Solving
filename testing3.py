def solve(n):
    divisors = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        return "YES"
    return "NO"


print(solve(6))
