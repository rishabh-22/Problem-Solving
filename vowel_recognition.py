n = int(input())

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
for _ in range(n):
    word = input()
    count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            count += (len(word) - i) * (i + 1)
    print(count)
