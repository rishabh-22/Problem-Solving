people = dict()
n = int(input())

for i in range(n):
    data = input()
    temp = data.split()
    people[temp[0]] = int(temp[1])

while True:
    name = input()
    if name == "" or name == "\n":
        break
    else:
        try:
            print("{}={}".format(name, people[name]))
        except KeyError:
            print("Not found")
