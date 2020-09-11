n = int(input())
for i in range(1, n+1):
    output = ""
    if i % 3 == 0:
        output += "foo"
    if i % 5 == 0:
        output += "bar"
    if output == "":
        output = str(i)
    print(output)
