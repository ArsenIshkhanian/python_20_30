# import msvcrt
# import random
# import readchar

# n = int(input('Enter n: '))
# monkey_emoji = '🐵'
# monkey_row = random.randint(1, n)
# monkey_column = random.randint(1, n)
# banan= '🍌'
# banan_row = random.randint(1, n)
# banan_column = random.randint(1, n)
# bomb= "💣"
# bomb_row = random.randint(1, n)
# bomb_column = random.randint(1, n)
# zombi = "🧟"
# zombi_row = random.randint(1, n)
# zombi_column = random.randint(1, n)
# score=0
# life = 3 


# while True:

#     if monkey_row==banan_row and monkey_column==banan_column:
#         score+=1
#         banan_row = random.randint(1, n)
#         banan_column = random.randint(1, n)

#     elif score >= 3 and (monkey_row==bomb_row and monkey_column==bomb_column):
#         life -= 1
#         bomb_row = random.randint(1, n)
#         bomb_column = random.randint(1, n)

#     elif score >= 5 and (monkey_row==zombi_row and monkey_column==zombi_column):
#         life -= 1
#         zombi_row = random.randint(1, n)
#         zombi_column = random.randint(1, n)

#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == monkey_row and j == monkey_column:
#                 print(monkey_emoji, end=' ')
#             elif i == banan_row and j == banan_column:
#                 print(banan, end=' ')
#             elif (i == bomb_row and j == bomb_column) and score >= 3:
#                 print(bomb, end=' ')
#             elif (i == zombi_row and j == zombi_column) and score >= 5:
#                 print(zombi, end=' ')
#             else:
#                 print('*', end='  ')
#         print(' ')
#     print(f'{monkey_emoji} | {monkey_row} | {monkey_column}')


#     print('W|S|A|D')
#     print('Score:', score)
#     print(f"Life: {life}")
#     step = readchar.readchar()
#     step = step.lower()

#     if step == 'w':
#         if monkey_row == 1:
#             monkey_row = n
#         else:
#             monkey_row -= 1

#     elif step == 's':
#         if monkey_row == n:
#             monkey_row = 1
#         else:
#             monkey_row += 1

#     elif step == 'a':
#         if monkey_column == 1:
#             monkey_column = n
#         else:
#             monkey_column -= 1

#     elif step == 'd':
#         if monkey_column == n:
#             monkey_column = 1
#         else:
#             monkey_column += 1

#     if monkey_row == zombi_row and monkey_column == zombi_column and score >= 5:
#         life -= 1
#     if score >= 5:
#         zombi_step = random.choice('awsd')
#         if zombi_step == 'w':
#             if zombi_row > 1:
#                 zombi_row -= 1
#             else:
#                 print("kapiky chi karox durs gal xaxadashtic")

#         elif zombi_step == 's':
#             if zombi_row < n:
#                 zombi_row += 1
#             else:
#                 print("kapiky chi karox durs gal xaxadashtic")

#         elif zombi_step == 'a':
#             if zombi_column > 1:
#                 zombi_column -= 1
#             else:
#                 print("kapiky chi karox durs gal xaxadashtic")

#         elif zombi_step == 'd':
#             if zombi_column < n:
#                 zombi_column += 1
#             else:
#                 print("kapiky chi karox durs gal xaxadashtic")

#     if life==0: 
#         print(f"Life: {life}")
#         print("Game over")
#         break

#     elif step == 'q':
#         break
#     else:
#         print("sxal tvyal")



# age = ('Arsen', 6, 6.4, 'inchvor@gmail.com')
# for i in age:
#     print(i)


# digit = [7, 'Arsen', [6, 5, 4]]
# print(digit[2])
# print(type(digit))
# print(digit[1:])

# digits = [10, 6, 7, 1, 2, 3]
# digits.sort(reverse=True)
# print(digits)


# name = 'Arsen'
# name = name.upper()
# print(name)


# names = ['is', 'Arsen', 'Hermine', 'Levon', 'Astghik', 'are', 'Shavarsh']
# names.sort(key=len, reverse=True)
# print(names)


# letters = ['a', 'b', 't']
# letters.sort()
# print(letters)


# list_ = [1, 2, 3, 4, 5, 6]
# list_.append(7)
# list_.insert(2, 8)
# list_[3] = 8
# list_.append([9, 8, 7, 6])
# list_.extend([9, 8, 7, 6])
# print(list_)
# x = [1, 2, 4]
# y = [6, 4, 3]
# z = x + y
# print(z)

# list_ = [1, 2, 3, 2, 1, 2, 3]
# print(list_.count(1))
# print(list_.index(3))

# list_ = [1, 2, 3, 2, 1, 2, 3]
# list_.remove(1)
# removed_element = list_.pop()
# print(removed_element)
# print(list_)
# del list_[2:]
# print(list_)
# list_.pop(3)
# print(list_)

# from copy import deepcopy


# x = [1, 2, [3, [4, [5]]], 6]
# y = deepcopy(x)
# y = list(x)
# y = x[::]
# y = x[:]
# x[2][1][1][0] = 7
# print(y)
# print(x)


# list_ = [1, 7, 3, 4]
# list_.clear()
# list_ = []
# list_ = [None]
# print(list_ * 10)
# list2 = list_[::-1]
# list_.reverse()
# print(list_)
# print(list2)



# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = []
# for i in x:
#     if i % 2 == 0:
#         y.append(i)

# print(y)
# y = [i for i in x if i % 2 == 0]


# y = ['Zuyg' if i % 2 == 0 else 'Kent' for i in x]
# x = [[2, 3], [4, 5, 6], [8, 9, 10]]


# y = [i for element in x for i in element]
# y=[]

# for element in x:
#     for i in element:
#         y.append(i)

# print(y)


# x = [1, 2, 3, 4, 5, 6]
# print(max(x))
# print(min(x))


# x = ['is', 'are', 'maximum']
# print(max(x, key=len))
# print(min(x, key=len))


# x = [1, 2, 3, 4]
# y = ['a', 'b', 'c', 'd']
# for i, k in zip(x, y):
#     print(i, k)
# for i in range(len(x)):
#     print(f'{i} - {x[i]}')


# for index, value in enumerate(x):
#     print(index, value)

# x = [1, 2, 3, [4, 5, 6]]
# y = [5, 4, 3]
# # x.append(y)
# print(x)
# z = x + y
# x.extend(y)
# print(z)


# digit = int(input())
# while True:
#     digit = int(input('Enter the digit: '))
    


# import math

# print(abs(-2))

# nums = [10, 3, 20, 8, 15]
# min_diff = 0
# value1 = 0
# value2 = 0
# for i in nums:
#     min_diff += i # 56
# nums.sort(reverse=True)  # [20, 15, 10, 8, 3] 
# for i in range(len(nums) - 1):
#     diff = nums[i] - nums[i + 1]
#     if diff < min_diff:
#         min_diff = diff
#         value1 = nums[i]
#         value2 = nums[i + 1]
# print(min_diff)
# print(value1, value2)           


# print(sum(nums))

# y = []
# while True:
#     x = int(input('X: '))
#     if x == 0:
#         break
#     else:
#         if x in y:
#             continue
#         else:
#             y.append(x)
# print(y)