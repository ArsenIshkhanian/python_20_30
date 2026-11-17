# x = 5
# print(type(x))


# x = list()
# print(type(x))


# class Human:

#     money = 8000

#     def __init__(self, name, surname, age, unecvatsq=0):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.unecvatsq = unecvatsq

#     def eat(self):
#         return f'{self.name}-y haca utum'

#     def sleep(self):
#         print(f'{self.name}-y qnatsa')

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def play(self):
#         print(f'{self.name} is playing')

# human_1 = Human('Arsen', 'Ishkhanian', 22) #exmp, instance
# print(human_1.unecvatsq)
# human_2 = Human('Levon', 'Baraghamyan', 24, 150000)
# print(human_2.unecvatsq)
# dog = Animal('Jeko')
# dog.play()
# action_1 = human_1.eat()
# print(action_1)
# print(human_2.eat())

# husband = Human('Anun', 'Azganun', 0)
# wife = Human('Anun', 'Azganun', 0)
# Human.money -= 3000
# print(wife.money)

# class Bankaccount:

#     def __init__(self, name, card_number, balance=0):
#         self.name = name
#         self.card_number = card_number
#         self.balance = balance
#         self.history = []

#     def deposit(self, money):
#         self.balance += money
#         self.history.append(f'Credit Account +${money}')

#     def withdraw(self, money):
#         if money <= self.balance:
#             self.balance -= money
#             self.history.append(f'Debit Account -${money}')
#         else:
#             print(f'Dear {self.name} -> Not enough fund!')

#     def transfer(self, other, money):
#         if money <= self.balance:
#             self.balance -= money
#             self.history.append(f'Debit card number to {other.card_number}|{other.name} -${money}')
#             other.balance += money
#             other.history.append(f'Credit card number from {self.card_number}|{self.name} +${money}')
#         else:
#             print(f'Dear {self.name} -> Not enough fund!')

#     def show_history(self):
#         print(f'{self.name} HISTORY')
#         for action in self.history:
#             print(action)
#             print('-'*10)

#     def get_balance(self):
#         return self.balance

# user_1 = Bankaccount('Levon Baraghamyan', '4083 0600 1111 2255', 25000)
# user_2 = Bankaccount('Shavarsh Karapetyan', '4083 8900 1045 6788')
# user_3 = Bankaccount('Astghik Arabyan', '4578 8900 9765 1111', -45000)
# user_1.transfer(user_2, 5000)
# user_2.deposit(20000)
# user_2.transfer(user_3, 25000)
# user_3.withdraw(25000)

# print(f'{user_1.name} account -> {user_1.get_balance()}')
# print(f'{user_2.name} account -> {user_2.get_balance()}')
# print(f'{user_3.name} account -> {user_3.get_balance()}')

# print('\n')
# user_1.show_history()
# user_2.show_history()
# user_3.show_history()


# class Triangle:

#     def  __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def status(self):
#         return self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b 

# er_1 = Triangle(12, 4, 5)
# er_2 = Triangle(100, 1, 1)
# print(er_1.status())


# class Listik:

#     def __init__(self):
#         self.memory = [None]*10

#     def append(self, element):
#         for index in range(len(self.memory)):
#             if self.memory[index] == None:
#                 self.memory[index] = element
#                 break

#     def __str__(self):
#         sequence = ''
#         for i in range(len(self.memory)):
#             if i == 0:
#                 sequence += f'[{self.memory[i]}'
#             elif i == len(self.memory) - 1:
#                 if self.memory[i] == None:
#                     sequence += ']'
#                 else:
#                     sequence += f'{self.memory[i]}]'
#             elif self.memory[i] != None:
#                 sequence += f', {self.memory[i]}'

#         return sequence

# x = Listik()
# x.append(5)
# x.append(4)
# x.append(2)
# x.append(1)
# print(x)

import random
sequence = ''
for i in range(4):
    if i == 0:
        pass
    else:
        sequence += ' '
    for j in range(4):
        if i == 0 and j == 0:
            sequence += str(random.randint(1, 9))
        sequence += str(random.randint(0, 9))
print(sequence)