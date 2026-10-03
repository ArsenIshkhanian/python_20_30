# keyboard = {
#     '1': ['.', ',', '?', '!', ':'],
#     '2': ['A', 'B', 'C'],
#     '3': ['D', 'E', 'F'],
#     '4': ['G', 'H', 'I'],
#     '5': ['J', 'K', 'L'],
#     '6': ['M', 'N', 'O'],
#     '7': ['P', 'Q', 'R', 'S'],
#     '8': ['T', 'U', 'V'],
#     '9': ['W', 'X', 'Y', 'Z'],
#     '0': ' '
# }

# text = input('Text: ').upper()

# for i in text:
#     for j in keyboard:
#         if i in keyboard[j]:
#             index = keyboard[j].index(i) + 1
#             print(j * index, end=' ')



# info = {
#     1: 'AEILNORSTU',
#     2: 'DG',
#     3: 'BCMP',
#     4: 'FHVWY',
#     5: 'K',
#     8: 'JX',
#     10: 'QZ'
# }

# text = input('Text: ').upper()
# summ = 0

# for i in text:
#     for j in info:
#         if i in info[j]:
#             summ += j

# print(summ)

# users = {}
# while True:
#     name = input('Enter your name: ')
#     if name.lower() == 'q':
#         break
#     email = input('Enter your email: ')
#     password = input('Enter your password: ')
#     users[name] = {
#     'email': email,
#     'password': password
#     }    

# for user in users:
#     print(f"{user} -> {users[user]['email']} - {users[user]['password']}")



# nums = [1, 8, 2, 3, 4, 5, 6, 7,9, 10]
# target = 9
# seen = {}

# for i in nums:
#     if i in seen:
#         print(i, seen[i])
#     else:
#         x = target - i
#         seen[x] = i


# x = [1, 2, 2, 3, 4, 2, 16, 1]
# y = set(x)
# print(y)

# x = {}
# x = set()

# x = {1, 2, 3, 4}
# y = {5, 7, 3, 6}
# x.add(5)
# x.discard(6)
# x.update(y)
# y.update(x)
# print(6 in x)
# print(x.issuperset(y))
# print(y.issubset(x))
# print(x.difference(y))
# print(y.difference(x))
# print(x.intersection(y))
# print(x.isdisjoint(y))
# x.pop()
# print(x)
# print(y)


# def fx():
#     print(10)

# fx() + 5

# def arsen():
#     return 10


# x = arsen()
# print(x + 5)


# def loop():
#     for i in range(15):
#         print(i)

# loop()


# def loop():
#     for i in range(1, 11):
#         for j in range(1, 11):
#             print(i * j, end='\t')
#         print()

# for i in range(10):
#     print(f'loop {i + 1}')
#     loop()


# def armat(tiv):
#     return tiv ** 0.5
# x = armat(int(input('N: ')))
# print(x)
# x = 16
# print(armat(x))


# def astichan(tiv, astichan, bajanarar):
#     return tiv ** astichan, bajanarar

# x = astichan(3, bajanarar=4, astichan=5)
# print(x)



# def x(*args):
#     print(args)


# x(1, 2, 3, 4)
# x(5, 6, 7)



# def x(**kwargs):
#     print(kwargs)


# x(b=4, d=5, k=6)


# def x(*args, **kwargs):
#     print(args)
#     print(kwargs)

# x(1, 2, 3, 4, k=5, y=5)


# import urish
# x = urish.armat(36)
# print(x)



# x = 5
# def func():
#     global x
#     x += 2
    

# func()
# print(x)


# def f1(a):
#     a += 2
#     def f2(a, b):
#         return a + b
#     return f2(a, a*2)
# x = f1(4)
# print(x)


# x = lambda a, b: a + b
# print(x(12, 6))


# def is_prime(digit):
#     for i in range(2, int(digit**0.5) + 1):
#         if digit % i == 0:
#             return False
#     return True


# def filter(elements):
#     prime_list = []
#     for element in elements:
#         if is_prime(element):
#             prime_list.append(element)
#     return prime_list

# elements = [i for i in range(3, 200)]
# prime_elements = filter(elements)
# print(prime_elements)

