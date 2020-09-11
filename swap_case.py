def swap_case(s):
    new = ""
    for i in s:
        if i.isupper():
            new += i.lower()
        elif i.islower():
            new.join(i.upper())
        else:
            new.join(i)

    # return s
    print(new)


swap_case("RishabH")

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
