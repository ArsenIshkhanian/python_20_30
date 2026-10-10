# import random
# def password_gen():
#     password = ''
#     length = random.randint(7, 10)
#     for _ in range(length):
#         element = random.randint(33, 126)
#         element = chr(element)
#         password += element

#     print(password, len(password))
# password_gen()

# print(chr(97))
# print(ord('a'))




# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def nextPrime(n):
#     prime = n + 1
#     while not isprime(prime):
#         prime += 1
#     return prime

# num = int(input('Enter the number: '))
# print(nextPrime(num))



# num = int(input('Enter the number: '))
# result = 0
# for i in range(1, num // 2 + 1):
#     if num % i == 0:
#         result += i

# if result == num:
#     print('True')
# else:
#     print('False')    




# list_ = []
# while True:
#     number = input('Enter the number: ')
#     if number == '':
#         break
#     num = int(number)
#     list_.append(num)
    
# mean_value = int(sum(list_) / len(list_))

# data = {}

# for i in list_:
#     if i < mean_value:
#         data.setdefault('Below Average', []).append(i)
#     elif i > mean_value:
#         data.setdefault('Above Average', []).append(i)
#     else:
#         data.setdefault('A number equal to the mean value', []).append(i)

# print(mean_value)
# print()
# print('Below Average')
# if 'Below Average' in data:
#    print(', '.join(str(x) for x in data['Below Average']))
# else:
#     print('Absent')

# print()  

# print('Above Average')
# if 'Above Average' in data:
#    print(', '.join(str(x) for x in data['Above Average']))
# else:
#     print('Absent')

# print()    

# print('A number equal to the mean value')
# if 'A number equal to the mean value' in data:
#    print(', '.join(str(x) for x in data['A number equal to the mean value']))
# else:
#     print('Absent')



# data = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
#     'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
#     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
#     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
#     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
#     '3': '...--', '4': '....-', '5': '.....', '6': '....-',
#     '7': '--...', '8': '---..', '9': '----.', '0': '-----'
# }
# result = []
# text = input('Enter the text: ').upper()
# for i in text:
#     if i in data:
#         result.append(data[i])
# morse_output = ' '.join(result)
# print(morse_output)


# x = [1, 2, 3, 4]
# # x.remove(3)
# del x[1]
# print(x)


# data = {
#         'D': 56, 
#         'E': 12, 
#         'F': 69, 
#         'C': 45, 
#         'B': 23, 
#         'A': 67
#         }
# print(sorted(data, key=data.get))
# print({key:data[key] for key in sorted(data, key=data.get, reverse=True)[:3]})


# x = {1, 2, 3}
# y = {1, 2, 4}
# print(y.issubset(x))


# x = lambda a, b: a + b
# print(x(5, 4))