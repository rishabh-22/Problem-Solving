# r, c = map(int, input().split())
# r, c = 9, 27
# for i in range(r):
#     # for j in range(c):
#     j = 1
#     while j <= c:
#         #     print(abs((c-3-(6*i))//2))
#         #     print(i*2+1)
#         # print('-' * abs((c-3-(6*i))//2) + '.|.' * (i*2+1) + '-' * abs((c-3-(6*i))//2))
#         if j < abs((c-3-(6*i))//2):
#             print('-', end="")
#         elif j == abs((c-3-(6*i))//2):
#             print('.|.' * (i*2+1), end="")
#         elif j > abs((c-3-(6*i))//2):
#             print('-', end="")
#         j += 1
#     print()
#  24 18 12 6
#  1 3 5 7 7 5 3 1

# n, m = map(int, input().split())
n, m = 9, 27
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print(pattern)
# print(pattern[::-1])
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
