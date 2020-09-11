def big_sorting(unsorted):
    # answer = list(map(int, unsorted))
    # answer.sort()
    unsorted.sort()
    answer = list(map(str, unsorted))
    return answer


if __name__ == '__main__':
    n = int(input())
    unsorted = list(map(int, input().split()))
    result = big_sorting(unsorted)

    print(result)
