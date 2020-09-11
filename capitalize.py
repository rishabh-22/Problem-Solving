def solve(s):
    name = ''
    flag = True
    for char in s:
        if flag and char != ' ':
            name += char.upper()
            flag = False
        elif char == ' ':
            name += char
            flag = True
        else:
            name += char
    print(name)


solve('hello   world  lol')

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()
