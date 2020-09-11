"""
finding percentage question was here.
"""


def calculate_percentage(data, name):
    marks = data[name]
    return sum(marks)/3


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(calculate_percentage(student_marks, query_name))
