"""to print 3 most occurring characters in a given string along with their occurrences."""

from collections import Counter


def word_count(string):
    final = {}
    data = dict(Counter(string))
    # print(data)
    data = sorted(data.items())
    # print(data)
    data = dict(data)
    for i in range(3):
        element = max(data, key=data.get)
        final[element] = data[element]
        data.pop(element)
    # print(final)

    ans = ''
    for k, v in final.items():
        ans += str(k)
        ans += " "
        ans += str(v)
        ans += "\n"

    print(ans)


word_count("qwertyuiopasdfghjklzxcvbnm")
