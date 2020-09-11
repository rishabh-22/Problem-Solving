def get_score(arr):
    # arr = sorted(arr, key=lambda x: x[1])
    scores = [x[1] for x in arr]
    scores = set(scores)
    scores = iter(scores)
    scores = sorted(scores)
    # next(scores)
    score = scores[1]
    names = []
    for student in arr:
        if student[1] == score:
            names.append(student[0])
    names.sort()

    print(*names, sep='\n')


if __name__ == '__main__':
    lis = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        lis.append(student)

    get_score(lis)
