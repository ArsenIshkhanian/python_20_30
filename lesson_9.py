# for i in range(2):
#     for j in 'ab':
#         print(i, j, end=' | ')
#     print()

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:<4}', end='')
#     print()


# n = int(input('N: '))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print('^', end=' ')
#         elif j == n + 1 - i:
#             print('^', end=' ')
#         else:
#             print(' ', end=' ')
#     print()




# a = int(input('A: '))
# b = int(input('B: '))

# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         if i == j:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# n = int(input('N: '))

# for i in range(1, n + 1):
#     for j in range(1, n + i):
#         if j >= n - i + 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# n = int(input('Enter the n: ')) # 5

# for i in range(1, n + 1):

#     for j in range(1, i + 1):
#         print(n + 1 - j, end=' ')

#     for k in range(2 * n - 2 * i):
#         print('-', end=' ')

#     for v in range(1, i + 1):
#         print(n - i + v, end=' ')

#     print()


# n = int(input('N: ')) # 5

# for i in range(n):
#     for j in range(n - i):
#         print(j + 1, end=' ')
#     print()



