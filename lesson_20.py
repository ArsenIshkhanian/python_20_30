# with open('some.txt', 'r') as file:
#     print(''.join(file.readlines()[:5]))
    # for i in range(10):
    #     print(file.readline().strip())



# with open('some.txt', 'r') as file:
#     print(''.join(file.readlines()[-6:]))



# data = {}
# with open('some.txt', 'r') as file:
#     content = file.read()
#     print(content)
#     for i in content:
#         i = i.upper()
#         if not i.isalnum():
#             continue
#         elif i in data:
#             data[i] += 1
#         else:
#             data[i] = 1
# print(data)



# data = {}
# with open('some.txt', 'r', encoding='utf-8') as file:
#     content = file.read().replace(',', '').replace('.', '').split(' ')
#     for i in content:
#         i = i.lower()
#         if i in data:
#             data[i] += 1
#         else:
#             data[i] = 1

# most_word = sorted(data, key=data.get, reverse=True)[0]
# print(most_word)


# with open('some.txt', 'r') as file:
#     conten = file.readlines()

# print(conten)

# with open('some.txt', 'w') as file:
#     for line in conten:
#         if line.startswith('#'):
#             continue
#         else:
#             file.write(line)




# boys_name = {}
# girls_name = {}
# for year in range(1900, 2013):
#     with open(f'BabyNames/{year}_BoysNames.txt', 'r') as file:
#         name = file.read().split()[0]
#         if name in boys_name:
#             boys_name[name] += 1
#         else:
#             boys_name[name] = 1

# for year in range(1900, 2013):
#     with open(f'BabyNames/{year}_GirlsNames.txt', 'r') as file:
#         name = file.read().split()[0]
#         if name in girls_name:
#             girls_name[name] += 1
#         else:
#             girls_name[name] = 1

# print(boys_name)
# print(girls_name)

import re

text = """
levon
hermine
shavarsh
Python 3.15 is the latest stable release of the Python programming language, with a mix of changes to the language, the implementation, and the standard library. 
The biggest changes include lazy imports, frozendict and sentinel builtins, UTF-8 as the default encoding, unpacking in comprehensions, and a stable ABI for free-threaded builds.
The library changes include a new profiling package with Tachyon, a high-frequency statistical sampling profiler, 
more color in command-line output as well as the usual deprecations and removals, 
and improvements in user-friendliness and correctness.
This article doesn’t attempt to provide a complete 4 specification of all new features,
but instead gives a convenient overview. For full details refer to the documentation, such as the Library Reference and Language Reference. 
To understand the complete implementation and design rationale for a change, refer to the PEP for a particular new feature;
but note that PEPs usually are not kept up-to-date once a feature has been fully implemented.
"""

# digits = []
# for i in text:
#     if i.isdigit():
#         digits.append(i)

# print(digits)

# content = re.findall('\d\.?\d*', text)
# print(content)


