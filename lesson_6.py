"""----------------------------Slide 1----------------------------"""

"""Exercise 1"""
# import random
# n = int(input('Enter the number: '))

# count = 0 #chmutsox
# for i in range(n): #0, 1, 2, 3, 4, ..., n-1
#     index = random.randint(0, 10)
#     debt = int(input(f'{index} Debt[{i + 1}]: '))
#     if index % 2 == 0 and debt > 0:
#         count += 1

# print(count)


"""Exercise 2"""
# total_salary = 0
# months = int(input('Enter the count of month: '))

# for i in range(months): 
#     salary = int(input(f'Enter the salary[{i + 1}]: '))
#     total_salary += salary


# avg = total_salary / months
# print(avg)


"""Exercise 3"""
# factorial = 1
# n = int(input('Enter the number of factorial: '))
# for i in range(1, n + 1):
#     factorial *= i

# print(factorial)


"""Exercise 4"""
# childrens = int(input("Enter the count of childrens: "))
# rank_5 = 0
# rank_4 = 0
# rank_3 = 0


# for i in range(childrens):
#     rank = int(input('Enter the rank: '))
#     if rank == 5:
#         rank_5 += 1
#     elif rank == 4:
#         rank_4 += 1
#     else:
#         rank_3 += 1


# if rank_5 >= rank_3 and rank_5 >= rank_4:
#     status = 'Gerazanc'
# elif rank_4 > rank_5 and rank_4 >= rank_3:
#     status = 'Harvatsayin'
# else:
#     status = 'Mijak'

# print(f'5 stacox - {rank_5}')
# print(f'4 stacox - {rank_4}')
# print(f'3 stacox - {rank_3}')
# print(f'Dzer dasarani status-y = {status}')


"""Exercise 5"""
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# count = 0
# summ = 0

# for i in range(a, b + 1):
#     if i % 3 == 0:
#         count += 1
#         summ += i

# avg = summ / count
# print(avg)


"""Exercise 6"""
#Version 1
# for i in range(10, 100):
#     f = int(str(i)[0])
#     s = int(str(i)[1])
#     if f * s == i / 3:
#         print(i)

#Version 2
# for i in range(10, 100):
#     a = i // 10 #veradardznum e arajin tivy
#     b = i % 10 #veradardznum e erkrord tivy
#     if a * b == i / 3:
#         print(i)


"""Exercise 7"""
# n = int(input('Enter the n: '))
# summ = n * (n+1) / 2

# for i in range(1, n):
#     lost_card = int(input('Enter the card: '))
#     summ -= lost_card

# print(int(summ))



"""----------------------------Slide 1----------------------------"""

"""Exercise 1"""
# a = int(input('Enter the number: '))
# b = int(input('Enter the number: '))

# if a == b:
#     print(a)
# elif a > b:
#     for i in range(a, a*b + 1, a):
#         if i % b == 0:
#             print(i)
#             break
# else:
#     for i in range(b, a*b + 1, b):
#         if i % a == 0:
#             print(i)
#             break


"""Exercise 2"""
# count_odd = 0
# count_even = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1

# print(f'Odd = {count_odd}')
# print(f'Even = {count_even}')


"""Exercise 3"""
# a = 0
# b = 1
# c = a + b
# for i in range(100):
#     print(a)
#     """Version1"""
#     # a = b
#     # b = c
#     # c = a + b
#     """"Version2"""
#     # a, b = b, a + b
#     if a > 40:
#         break


# a = 5
# b = 4
# c = a + b # 9
# a = c - a # 4
# b = c - a # 5
# a, b = b, a
# print(a, b)


# a = 4
# b = 5
# c = a * b
# a = c / a
# b = c / a
# print(a, b)



