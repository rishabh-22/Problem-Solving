n = int(input())
for i in range(n):
    arr = input().split()
    try:
        print(int(arr[0])//int(arr[1]))
    except Exception as e:
        print("Error code: {}".format(e))
