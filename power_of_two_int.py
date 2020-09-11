import math


def is_power(n):
    if n == 1:
        return True

    # Try all numbers from 2 to sqrt(n) as base
    for x in range(2, int(math.sqrt(n)) + 1):
        y = 2
        p = int(math.pow(x, y))

        # Keep increasing y while power 'p' is smaller
        # than n.
        while n >= p > 0:
            if p == n:
                return True

            y = y + 1
            p = math.pow(x, y)

    return False


print(is_power(36659335873158286639659788399299112306681891089112663692520394699058876146592117791756650299930391607768110626996768959256264011561313782902130308522207873078199594424249047090278789080616351985169389566720792737398054347347040514961001414656))
