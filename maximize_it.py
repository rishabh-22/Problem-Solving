"""
receives a number of lists, chooses integers from that list to square and add.
the mod of that sum must be max, the number by which mod is to be done will also be received.
"""
import itertools
import os

lists = []


def maximize(lists, divisor):
    final = [p for p in itertools.product(*lists)]
    result = []
    # print(lists, divisor)
    # print("final:", final)
    for item in final:
        s = 0
        for it in item:
            s += it**2
        result.append(s % divisor)
    print(result)
    print(max(result))
    return str(max(result))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = list(map(int, input().rstrip().split()))

    for t_itr in range(arr[0]):
        t_itr = list(map(int, input().rstrip().split()))
        lists.append(t_itr)

    result = maximize(lists, arr[1])

    fptr.write(result)
    fptr.write('\n')

    fptr.close()
