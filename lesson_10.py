# n = int(input('N: '))

# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()


# n = int(input('N: '))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# n = int(input("n= "))

# for i in range(1, n):
#     for j in range(1, n):
#         if i % 2 !=0:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()


# n = int(input('n: '))

# for i in range(n):
#     for j in range(1, n + 1 - i):
#         print(j, end=' ')
#     print()


# n = int(input('n: '))

# for i in range(n):
#     for j in range(n + 1 - i):
#         print(j, end=' ')
#     print()



# n = int(input('N: '))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j > n + 1 - i:
#             print('.', end=' ')
#         else:
#             print('#', end=' ')
#     print()


# n = int(input('n: '))

# for i in range(2, n + 1):
#     summ = 0
#     for j in range(1, i):
#         if i % j == 0:
#             summ += j

#     if summ == i:
#         print(i)


# x = 1

# print(f'{x} + {6 - x} = {6}')
# print(f'{x + 1} + {6 - (x + 1)} = {6}')
# print(f'{x + 2} + {6 - (x + 2)} = {6}')
# print(f'{x + 3} + {6 - (x + 3)} = {6}')
# print(f'{x + 4} + {6 - (x + 4)} = {6}')


# n = int(input('N: ')) # 6

# for i in range(1, n):
#     print(f'{i} + {n - i} = {n}')



# n = int(input('N: '))
# for i in range(1, n + 1):
#     k = 1
#     for j in range(1, n + i):
#         if j >= n + 1 - i:
#             print(k, end=' ')
#             if j >= n:
#                 k -= 1
#             else:
#                 k += 1
#         else:
#             print(' ', end=' ')
#     print()


# import msvcrt
# import random
# import readchar

# n = int(input('Enter n: '))
# monkey_emoji = '🐵'
# monkey_row = random.randint(1, n)
# monkey_column = random.randint(1, n)


# while True:

#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == monkey_row and j == monkey_column:
#                 print(monkey_emoji, end=' ')
#             else:
#                 print('*', end='  ')
#         print(' ')

#     print('W|S|A|D')
#     step = readchar.readchar()
#     step = step.lower()

#     if step == 'w':
#         monkey_row += 1