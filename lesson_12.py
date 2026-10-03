# nums = [4, 6, 8, 18, 10]

# for i in range(len(nums)): #0, 1, 2, 3, 4
#     nums[i] *= 2

# print(nums)


# nums = [4, 6, 8, 18, 10]
# y = []
# for i in nums:
#     y.append(i * 2)
# print(y)


# words = ['is', 'are', 'the best', 'python', 'c++', 'Javascript']

# longest_word = max(words, key=len)
# print(longest_word)

# words.sort(key=len, reverse=True)
# print(words[0])

# longest_word = ''
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)




# x = [10, 12, 4, 5, 3, 2, 8]
# y = [11, 8, 7, 2, 19, 20]
# status = False
# for i in x:
#     for j in y:
#         if i == j:
#             print(i)
#             status = True
#             break
#     if status:
#         break


# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# yndhanur_arzheq = False
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             yndhanur_arzheq = True
# print(yndhanur_arzheq)

# text = '*'
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())


# password = 'Python@$World11'
# count_digit = 0
# count_sym = 0
# for i in password:
#     if i.isdigit():
#         count_digit += 1
#     elif not i.isalnum():
#         count_sym += 1

# if len(password) >= 8 and count_sym >= 2 and count_digit >= 2:
#     print('Strong')

# text = 'p y t h o n'
# print(text.split())

# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# print(link.split('=')[1])
# id_ = ''
# status = False
# for i in link:
#     if i == '=':
#         status = True
#         continue

#     if status:
#         id_ += i
# print(id_)
    

# list1 = [1, 2, 3, 4, 8]
# list2 = [5, 6, 7, 8, 9]

# i = 0
# j = 0
# while i < len(list1) and j < len(list2):
    
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# i = 0
# j = 0
# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         i += 1
#     elif list1[i] > list2[j]:
#         j += 1
#     else:
#         print(list1[i])
#         break


# text = 'A man, a plan, a canal, Panama!'
# print(text[::-1] == text)
# text = text.lower().replace(' ', '').replace('!', '').replace(',', '')
# print(text)
# print(text[::-1] == text)


# digits = input('Digits: ') # 12 21 14 53
# y = digits.split()
# print(y)
# for i in y:
#     if int(i) % 2 == 0:
#         print(i)


# x = [19, 8, 10, 12, 14, 16, 18, 20, 21, 34, 55, 63, 90]

# for i in x:
#     if i % 2 == 0:
#         x.remove(i)

# print(x)


# x = [19, 8, 10, 12, 14, 16, 18, 20, 21, 34, 55, 63, 90]

# for i in x[::-1]:
#     if i % 2 == 0:
#         x.remove(i)

# print(x)

# i = 0
# while i < len(x):
#     if x[i] % 2 == 0:
#         x.remove(x[i])
#     else:
#         i += 1
# print(x)

# import random

# yntroxner = ['Arsen', 'Astghik', 'Shavarsh', 'Levon', 'Hermine']
# yntrvoxner = ['Arsen', 'Astghik', 'Shavarsh', 'Levon', 'Hermine']

# while yntroxner != []:
#     status = False
#     yntrox = random.choice(yntroxner)
#     yntrvox = random.choice(yntrvoxner)
#     while yntrox == yntrvox:
#         yntrvox = random.choice(yntrvoxner)
#         if len(yntroxner) == 1:
#             status = True
#             break
#     print(f'1){yntrox} -> {yntrvox}')
#     yntroxner.remove(yntrox)
#     yntrvoxner.remove(yntrvox)
#     if status:
#         yntroxner = ['Arsen', 'Astghik', 'Shavarsh', 'Levon', 'Hermine']
#         yntrvoxner = ['Arsen', 'Astghik', 'Shavarsh', 'Levon', 'Hermine']