# import time
# n = int(input('Enter the timer: '))

# for i in range(n, 0, -1):
#     time.sleep(1)
#     answer = input('Do you want to take your food(1/0): ')
#     if answer == '1':
#         print(f'Qo mikrovalnovken hly uner {i - 1} vayrkyan.')
#         break

# print('You food is ready!!!')



# start = int(input('Enter the start: '))
# end = int(input('Enter the end: '))
# step = int(input('Enter the step: '))

# for x in range(end, start - 1, step):
#     summ = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print(f'{x} - {summ}')


# tsrar = 12
# letter_size = int(input('namak: '))
# tsalel = 0

# for i in range(100):
#     print(f"Namak = {letter_size}")
#     if letter_size > tsrar:
#         letter_size //= 2
#         tsalel += 2
#     else:
#         break

# print(f'Duq tsalel eq {tsalel} angam')


# toshak = int(input("mutqagreq toshaki tivy: "))
# tsaxs = int(input("mutqagreq tsaxsi tivy: "))
# total_tsaxs = 0
# ynd_toshak = toshak * 10
# for i in range(1, 11):

#     total_tsaxs += tsaxs
#     tsaxs *= 1.03

# tarberutyun = total_tsaxs-ynd_toshak
    
# print(f"cnoxneric petq e avel verdzni {round(tarberutyun)} dram") 


# import fractions

# digit = fractions.Fraction(5/4)
# print(digit + 4)

# number = 1
# n = int(input('n: '))

# for i in range(n):
#     number -= (-1)**i * (1 / (2**(i+1)))


# print(number)


# actions = 7
# hamarich = 1
# haytarar = 1
# x = int(input('x: ')) # 13

# for i in range(1, actions):
#     hamarich *= (x - (2**i - 1))
#     haytarar *= (x - 2**i)

# res = hamarich / haytarar
# print(res)



#By Levon
# actions = 65
# hamarich = 1
# haytarar = 1
# x = int(input('x: ')) # 13

# for i in range(1, actions):
#     if i % 2 == 1:
#         hamarich *= (x - i)
#     else:
#         haytarar *= (x - i)

# res = hamarich / haytarar
# print(res)


# boys = int(input('Boys: '))
# girls = int(input('Girls: '))

# if boys > 2 * girls or girls > 2 * boys:
#     print('Dzev chka')
# elif boys > girls:
#     diff = boys - girls
#     skizb = diff * 'TAT'
#     A = skizb.count('A')
#     A = girls - A
#     print(skizb + A*'TA')
# elif boys == girls:
#     print(boys * 'TA')
# else:
#     diff = girls - boys
#     skizb = diff * 'ATA'
#     T = skizb.count('T')
#     T = boys - T
#     print(skizb + T*'AT')



# import random
# import time
# name = input('Enter your name: ')
# ready = input(f'Dear {name} are you ready(yes/no)? ').lower()
# if ready == 'yes':
#     comp_score = 0
#     user_score = 0
#     print(3)
#     time.sleep(0.7)
#     print(2)
#     time.sleep(0.7)
#     print(1)
#     time.sleep(0.7)
#     print("Let's Go")
#     round = int(input('How many round do you want to play? '))
#     for i in range(1, round + 1):
#         title = f'Round {i}'
#         print()
#         print(title.center(30, '-'))
#         comp_number = random.randint(1, 5)
#         print(f'Yngers ete inch compy pahela {comp_number}-y')
#         user_number = int(input('Guess the number from 1 to 5: '))
#         if user_number == comp_number:
#             user_score += 1
#             print(f'Comp - {comp_number} | {name} - {user_number}')
#             print(f"Dear {name} you win this round!!!")
#             print(f"Comp score = {comp_score} / {name} score = {user_score}")
#         else:
#             comp_score += 1
#             print(f'Comp - {comp_number} | {name} - {user_number}')
#             print(f"Comp win this round!!!")
#             print(f"Comp score = {comp_score} / {name} score = {user_score}")
# else:
#     print('Du gites')

# print()

# if comp_score > user_score:
#     print('Overall Comp win this game')
# elif comp_score < user_score:
#     print(f'{name} win this game ')
# else:
#     print('Draw!!!!!!!!!!!!!!!!!!!')



# i = 0
# while i < 5:
#     print(i)
#     i += 1

# x = 5
# while x != 0:
#     print(x)
#     x += 1


# while True:
#     name = input('Enter your name: ')
#     if name != '':
#         break


# while True:
#     move = input('Enter the movement A|W|D|S, if you want to exit game press \'q\': ').lower()
#     if move == 'q':
#         break
#     print(move)


# summ = 0
# count = 0
# while True:
#     number = int(input('Enter the number: '))
#     if number == 0:
#         break
#     summ += number
#     count += 1
# print(summ / count)


# summ = 0

# while True:
#     age = int(input('Enter the age: '))
#     if age == 0:
#         break
#     elif age < 6:
#         continue
#     elif age < 18:
#         summ += 1000
#     elif age < 63:
#         summ += 1500
#     else:
#         summ += 700

# print(f'Summan = {summ}')



# import random
# count_O = 0
# count_P = 0
# while count_O != 5 and count_P != 5:
#     choice = random.choice('OP')
#     print(choice, end='')
#     if choice == 'O':
#         count_O += 1
#         count_P = 0
#     else:
#         count_P += 1
#         count_O = 0


 