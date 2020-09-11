with open("freshers/test.txt", "w+") as file:
    file.write("line1\nline2\nline3\nline4\nline5")

with open("freshers/test.txt") as fi:
    for line in fi.readlines():
        a = line
        print(a)
