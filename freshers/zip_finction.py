from functools import reduce


def multiply_index(arr1, arr2):
    multiply = zip(arr1, arr2)
    for i in multiply:
        print(reduce(lambda a, b: a * b, i))


multiply_index([1, 2, 3, 4], [1, 2, 3, 4])
