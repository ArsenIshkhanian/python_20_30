# data = {}
# print(type(data))


# data = {'name': 'Arsen', 'age': 45, 'x': 'y'}

# data = {
#     'name': 'Arsen',
#     'age': 45,
#     'x': 'y'
# }

# print(data)
# print(data.keys())
# print(data.values())
# print(data.items())
# info = [('name', 'Arsen'), ('age', 45), ('x', 'y')]
# print(dict(info))


# data = {
#     [1, 2, 3]: 'Arsen',
#     'age': 45,
#     'x': 'y'
# }


# data = {
#     'a': 1,
#     'b': 2,
#     'a': 3
# }
# print(data)


# data = {
#     'a': 6,
#     'c': 4,
#     'd': -5,
#     'b': 2
# }

# print(len(data))

# print(data[0])

# for i in data:
#     print(i, data[i])

# print('-'*50)

# for key, value in data.items():
#     print(key, value)

# for i in data.values():
#     print(i)


# data = {
#     'a': 6,
#     'c': 4,
#     'd': -5,
#     'b': 2
# }

# data['w'] = 7
# print(data)

# x = {
#     'a': 6,
#     'c': 4,
#     'd': -5,
#     'b': 2
# }

# y = x.copy()
# y = dict(x)
# x['w'] = 7
# print(y)


# data = {
#     'a': 6,
#     'c': 4,
#     'd': -5,
#     'b': 2
# }

# data.popitem()
# data.pop('a')
# print(data)
# data.clear()
# data = {}
# print(data)
# data.setdefault('b', 77)
# print(data)

# data['b'] = 15
# print(data)

# print(data['k'])
# print(data.get('b', 'Chka tenc tar'))

# print(dict.fromkeys(['a', 'b', 'c'], 2))


# data = {
#     'arsen_08': {
#         'email': 'vwsve@gmail.com',
#         'password': '12412vdwvw'
#     },
#     'Levon_________________': {
#         'email': 'vwedvw',
#         'password': 'wevvfv'
#     }
# }


# data = {
#     'Arsen': [19, 20, 20, 18],
#     'Astghik': [2, 5, 12, 6],
# }


# data = {
#     'a': 6,
#     'c': 4,
#     'd': -5,
#     'b': 2
# }

# summ = 0
# for key in data:
#     print(key, data[key])
#     summ += data[key]

# print(summ)

# data = {
#     'a': 6,
#     'c': 4,
#     'd': -5,
#     'b': 2
# }

# print({key: data[key] for key in sorted(data, key=data.get)})

# new_dict = {}
# for key in sorted(data, key=data.get):
#     new_dict[key] = data[key]
# print(new_dict)


# print(sorted(data))
# print(sorted(data.values()))
# print(sorted(data, key=data.get))

# print([i for i in range(15) if i % 2 == 0])
# print([i for i in range(15)])
# list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([value for element in list_ for value in element])

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(['Zuyg' if value % 2 == 0 else 'Kent' for value in list_])


# person = {
#     "name": "Anna",
#     "age": 20,
#     "city": "Yerevan",
# }
#Ex 1
# print(person)
# print(person['name'])
# print(person['city'])

#Ex2
# person['gender'] = 'Female'
# print(person)

#Ex3
# for key in person:
#     print(f'{key} -> {person[key]}')

#Ex4
# students = {
#     "Anna": 85,
#     "John": 92,
#     "David": 78,
#     "Maria": 95
# }
# if 'Anna' in students:
#     students['Anna'] += 1
# else:
#     students['Anna'] = 86
# score = 0
# name_m = ''

# for name in students:
#     if students[name] > score:
#         score = students[name]
#         name_m = name

# print(name_m, score) 


#Ex5
# text = input('Text: ')
# new_dict = {}
# for letter in text:
#     if letter in new_dict:
#         new_dict[letter] += 1
#     else:
#         new_dict[letter] = 1

# print(new_dict)

# print({letter:text.count(letter) for letter in text})
# dict_ = {}
# for letter in text:
#     dict_[letter] = text.count(letter)
# print(dict_)


#Ex6
# numbers = [4, 2, 4, 1, 2, 4, 3]
# new_dict = {}

# for number in numbers:
#     if number in new_dict:
#         new_dict[number] += 1
#     else:
#         new_dict[number] = 1

# maximum_count = 0
# max_digit = 0
# for digit in new_dict:
#     if new_dict[digit] > maximum_count:
#         maximum_count = new_dict[digit]
#         max_digit = digit

# print(max_digit, maximum_count)