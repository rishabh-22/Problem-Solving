def swap_case(s):
    new = []
    for i in s:
        if i.isupper():
            new.append(i.lower())
        elif i.islower():
            new.append(i.upper())
        else:
            new.append(i)
    return "".join(new)


print(swap_case("Rishabh !@#$5678"))

