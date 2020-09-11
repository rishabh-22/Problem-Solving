from collections import defaultdict


def get_canonical(word):
    return "".join(sorted(word))


def group_anagrams(words):

    # words = sorted(words)
    dic = defaultdict(lambda: [])
    for i in words:
        # cp = i
        cf = get_canonical(i)
        dic[cf].append(i)
        # temp.append("".join(sorted(i)))

    final = []
    for k, v in dic.items():
        final.append(v)

    # print(dic.items())
    print(final)


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
