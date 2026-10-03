# age = int(input('Enter your age: '))
# pasport_status = input('Do you have a passport(yes/no)? ').lower()
# destination = input('Where do you want to go? ').title()
# print(age >= 18 and pasport_status == 'yes' and destination != 'North Korea')



# import time
# import random
# loading_time = random.randint(1, 10)
# print(loading_time)
# time.sleep(loading_time)
# print(loading_time <= 5)


# x = 5
# y = 4
# print(x > y)
# if x < y:
#     print('x is max')


# print('meka tpeluem')

# text = input('Enter the text: ')
# if len(text) >= 1:
#     print(f'goyutyun uni {text}')


# x = int(input('Enter x: '))
# y = int(input('Enter y: '))

# if x > y:
#     print('x is max')
# elif x < y:
#     print('y is max')
# else:
#     print('x == y')


# vowels = 'aeiou'
# letter = input('Enter letter: ')

# if letter in vowels:
#     print(f'{letter} is vowel')
# else:
#     print(f'{letter} is consonant')



# name = input('Enter name: ')
# if name:
#     print(f'Barev {name} jan')
# else:
#     print('Gone anund gri')

# if 'i':
#     print('Katarec')
# else:
#     print('Chkatarec')

# tar = 'a'
# if tar == 'i' or tar == 'u' or tar == 'a' or tar == 'e' or tar == 'o':
#     print('dvdvswdv')

# tar = input('tar: ')

# if tar == 'a' or 'i':

# print('k' or 'p' in 'python')

# x = int(input('Enter x: '))

# if x > 0:
#     print('x drakan e')
#     if x < 10:
#         print('x 10-ic poqr e')
#     else:
#         print('x 10ic mets e')
# elif x < 0:
#     print('x bacasakan e')
#     if x < -10:
#         print('x poqr e -10-ic')
# else:
#     print('x = 0')

# x = 5

# if 10 >= x >= 0:
#     print('x ynkats e 0-ic 10 mijakayqum')



# exanak = input('Inch exanak e: ').lower()

# if exanak == 'andzrev':
#     print('Mna tany python ara')
# elif exanak == 'qami':
#     print('Taq hagnvi nor durs ari')
# elif exanak == 'arev':
#     bassein = input('Karoxa gnas basein? ').lower()
#     if bassein == 'ayo':
#         tex = input('Vortegh es uzum gnas? ').lower()
#         if tex == 'sevan':
#             print('Indz dzen chtas')
#         elif tex == 'dvin':
#             print('Ari hetevics')
#         else:
#             print('De qez lav or')
#     else:
#         avto_lval = input('Karoxa avton lvas? ')
#         if avto_lval == 'ayo':
#             print('shat lava')
#         else:
#             print('inch anhaves lakot es')
# else:
#     print('Normal exanak gri')



# import time
# import random

# name = input('Enter your name: ')
# play_status = input('Are you ready(yes/no)? ')
# if play_status == 'yes':
#     print(3)
#     time.sleep(0.7)
#     print(2)
#     time.sleep(0.7)
#     print(1)
#     time.sleep(0.7)
#     print("Let's go")
#     user_score = 0
#     comp_score = 0
#     comp_number = random.randint(1, 5)
#     user_number = int(input('Enter your choice(1, 5): '))
#     if user_number == comp_number: # es 1 comp 0
#         user_score += 1
#         print(f"User guess: {user_number} | Comp guess: {comp_number}")
#         print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Enter your choice(1, 5): '))
#         if user_number == comp_number: # es 2 comp 0
#             user_score += 1
#             print(f"User guess: {user_number} | Comp guess: {comp_number}")
#             print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Enter your choice(1, 5): '))
#             if user_number == comp_number: # es 3 comp 0
#                 user_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print(f'Winner is {name}')
#             else: # es 2 comp 1
#                 comp_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print(f'Winner is {name}')
#         else: # es 1 comp 1
#             comp_score += 1
#             print(f"User guess: {user_number} | Comp guess: {comp_number}")
#             print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Enter your choice(1, 5): '))
#             if user_number == comp_number: # es 2 comp 1
#                 user_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print(f'Winner is {name}')
#             else: #es 1 comp 2
#                 comp_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print(f'Winner is Comp')
#     else: #es 0 comp 1
#         comp_score += 1
#         print(f"User guess: {user_number} | Comp guess: {comp_number}")
#         print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Enter your choice(1, 5): '))
#         if user_number == comp_number: # es 1 comp 1
#             user_score += 1
#             print(f"User guess: {user_number} | Comp guess: {comp_number}")
#             print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Enter your choice(1, 5): '))
#             if user_number == comp_number: #es 2 comp 1
#                 user_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print(f'Winner is {name}')
#             else: # es 1 comp 2
#                 comp_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print(f'Winner is Comp')
#         else: #es 0 comp 2
#             comp_score += 1
#             print(f"User guess: {user_number} | Comp guess: {comp_number}")
#             print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Enter your choice(1, 5): '))
#             if user_number == comp_number:# es 1 comp 2
#                 user_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'{name} Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print('Winner is Comp')
#             else: #es 0 comp 3
#                 comp_score += 1
#                 print(f"User guess: {user_number} | Comp guess: {comp_number}")
#                 print(f'Comp Win!!>> {name} = {user_score} | Comp = {comp_score}\n')
#                 print('End Game')
#                 print('Winner is Comp')
# else:
#     print('Try Later')


# tar = input('Enter the lette: ')
# print(type(tar))


