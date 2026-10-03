# # xndir 1

# x = int(input("mutqagreq verjin tivy: "))

# i = 1
# while i <= x:
#     print(i ** 3)
#     i += 1


# # xndir 2

# i =0
# anun = input("mutqagreq dzer anumy: ")
# print(f"bari galust {anun} jan: ")
# partq = int(input(f"inchqan eq partq {anun} jan: "))
# print("petq e marenq amboxj gumary ")
# while i <=partq:
#     print(f"mnac vcharelu {partq-i} dram")
#     vchar = int(input("inchqan eq vcharum: "))
#     i+=vchar
# print("duq mareciq partqy \n shnorhakalutyun")

#xndir 3

# i=0
# x= int(input("mutqagreq tivy: "))
# while x != 0 and x != -1:
#     print(x)
#     x=x//10 
#     i+=1
# print(i)



#xndir 4
# i_drakan = 0
# i_bacasakan = 0 

# while True:
#     x = int(input("mutqagreq gnahatakannery: "))
#     if 100 >= x > 0:
#         i_drakan += 1
#     elif -100 <= x < 0:
#         i_bacasakan += 1
#     else:
#         break
# print(i_drakan, i_bacasakan)
#harcnel

#xndir 5
# xndir = 0
# zang = 0
# jam = 0

# while jam < 8:
#     x = int(input("Qani xndir e? "))
#     xndir += x

#     zang = int(input("kint a zangum verdznum es? 1-ayo, 0-voch: "))

#     if zang == 1:
#         patasxanel = 1

#     jam += 1

# print(xndir)

# if patasxanel == 1:
#     print("Nuzhno zayti v magazin")


# X = int(input('Avand: '))
# P = int(input('Tokos: '))
# Y = int(input('Nmatakaket: '))
# year = 0

# while Y > X:
#     X *= (1 + P/100)
#     year += 1

# print(year)


# import random

# comp_number = random.randint(1, 100) # 67

# while True:
#     user_number = int(input('Guess the number: '))
#     if user_number == comp_number:
#         print(f"You guess the number and the number - {comp_number}")
#         break
#     elif comp_number > user_number:
#         print(f"More than {user_number}")
#     else:
#         print(f"Less than {user_number}")
    



#Binary Search
# import math

# a = int(input('Enter the start: '))
# b = int(input('Enter teh end: ')) 
# count = 0

# while True:
#     print(f'a = {a}, b = {b}')

#     comp_number = math.ceil((a + b) / 2)

#     answer = input(f'Is your number {comp_number}(yes/less/more)? ').lower()
#     count += 1

#     if answer == 'yes':
#         print(f'Yeyyy, I guessed with {count} time.')
#         break
#     elif answer == 'less':
#         b = comp_number - 1
#     else:
#         a = comp_number + 1


# for i in range(1, 101):
#     print(i)

# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# for i in range(1, 101, 2):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)


# x = 5
# for i in range(1, x + 1):
#     print(f'{x} * {i} = {x * i}')

# summ = 0
# while summ < 100:
#     num = int(input('Enter the num: '))
#     summ += num
    
# print(summ)


# summ = 0
# for i in range(3, 101, 3):
#     # if i % 3 == 0:
#     summ += i
# print(summ)


# max_num = 0
# for num in range(10):
#     new_num = int(input('Enter the num: '))
#     if new_num > max_num:
#         max_num = new_num
# print(max_num)



# text = 'Python'
# for i in range(len(text)):
#     print(f'{i + 1} - {text[i]}')


# text = 'Python is the best programmin language.'
# for i in range(0, len(text), 2):
#     print(text[i], end='')



# number = int(input('Enter the number: '))
# print(number)
# while number != 1:
#     if number % 2 == 0:
#         number //= 2
#     else:
#         number = number * 3 + 1
#     print(number)




# text = 'aabbccccaaaaabbbbbccbbbbbbbbbbbb' # 25
# max_count = 0
# new_count = 1
# for i in range(len(text) - 1):
#     if text[i] == text[i + 1]:
#         new_count += 1
#     elif new_count > max_count: 
#         max_count = new_count
#         new_count = 1
#     else:
#         new_count = 1 

#     if i == len(text) - 2 and new_count > max_count:
#         print('mtav stex')
#         max_count = new_count

# print(max_count)


# text = 'Python'

# for i in range(len(text) - 1): #0, 1, 2, 3, 4, 5
#     print(f'{i} - {text[i]}')

#     if i == len(text) - 2:
#         pass





    
