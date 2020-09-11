from itertools import permutations
import enchant
from datetime import datetime
d = enchant.Dict("en_US")

input_list = ['t', 'r', 'a', 'i', 'n', 's', 'g', 'o', 'p']


def check_valid_words(words):
    permutation = []
    for i in range(3, len(words)+1):
        perm = permutations(words, i)
        permutation += list(perm)

    word_list = ["".join(tup) for tup in permutation]

    valid_words = []
    for word in word_list:
        if d.check(word):
            valid_words.append(word)

    return valid_words


start = datetime.now()
lis = check_valid_words(input_list)
end = datetime.now()
print(len(lis), lis)
print("Time taken:", end-start)
