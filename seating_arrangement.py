t = int(input())
for c in range(0, t):
    num = int(input())
    modVal = num % 12
    modDiv = num//12
    if modVal == 0:
        nextVal = 12*(modDiv-1)+1
    else:
        nextVal = (12-modVal+1) + 12*modDiv

    if modVal % 6 == 3 or modVal % 6 == 4:
        seat = 'AS'
    elif modVal % 6 == 0 or modVal % 6 == 1:
        seat = 'WS'
    else:
        seat = 'MS'

    print(f'{nextVal} {seat}')
