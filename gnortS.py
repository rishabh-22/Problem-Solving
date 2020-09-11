# word = input()
word = 'Sorting1234'
small = []
capital = []
odd_nums = []
even_nums = []
for char in word:
    if 96 < ord(char) < 123:
        small.append(char)
    elif 64 < ord(char) < 91:
        capital.append(char)
    elif char in ['1', '3', '5', '7', '9']:
        odd_nums.append(char)
    elif char in ['2', '4', '6', '8', '0']:
        even_nums.append(char)

small = sorted(small)
capital = sorted(capital)
odd_nums = sorted(odd_nums)
even_nums = sorted(even_nums)

ans = "".join(small + capital + odd_nums + even_nums)
print(ans)
