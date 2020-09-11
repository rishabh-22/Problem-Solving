def process(word):
    ans = []
    for i in word:
        try:
            if i == '#':
                ans.pop(-1)
            else:
                ans.append(i)
        except:
            continue
    return "".join(ans)


def backspace_compare(S, T):
    # ans = []
    s = process(S)
    t = process(T)

    if s == t:
        return True
    else:
        return False


print(backspace_compare("y#fo##f", "y#f#o##f"))