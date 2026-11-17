# cutoff = int(input('Enter the threshold value. '))
# less_than_cutoff = []
# greater_than_cutoff = []
# print('Enter integers(press Enter on an empty line to finish). ')
# while True:
#     user_input = input()
#     if user_input == '':
#         break
#     number = int(user_input)
#     if number < cutoff:
#         less_than_cutoff.append(number)
#     elif number > cutoff:
#         greater_than_cutoff.append(number)
# print('Result of dividing the numbers:')
# for i in less_than_cutoff:
#     print(i, end=' ')

# print('\n')    
# print(cutoff)
# print()
# for i in greater_than_cutoff:
#     print(i, end=' ')     



# areas = [
#     [-2.0, -1.0, -0.5, -0.5],
#     [-1, -0.5, 0.5, -0.5],
#     [-1.0, 0.5, 1.0, -0.5],
#     [-1.0, -0.5, -0.5, -1.0]
# ]

# s = 0
# count = 0
# for i in areas:
#     for j in i:
#         if j < 0:
#             s += abs(j)
#             count += 1

# print(round(s / count, 2))



# text = input('text: ').lower()
# print(text == text[::-1])



# def sum_of_l(letter, word):
#     return word.count(letter
# text = input("Text: ").lower()
# letter = input("Letter: ").lower()
# print(sum_of_l(letter, text))



# try:
#     x = 5
#     y = 6
#     print(x + y)
# except Exception as e:
#     print(e.__class__.__name__)
# else:
#     print('Else-i code')
# finally:
#     print('Finally code')




# try:
#     f = open(file='/Users/arsenishkhanian/Desktop/some.txt', mode='r', encoding='utf-8')
#     print(f.read())
# except FileNotFoundError:
#     pass
# print(f.read())
# print(f.readline())
# print(f.readlines())
# print(f.read().split('\n'))



# f = open(file='/Users/arsenishkhanian/Desktop/some.txt', mode='r', encoding='utf-8')
# print(f.read())
# f.close()



# with open('some.txt', 'r') as f:
#     print(f.read())
#     print(f.readline())
#     print(f.readlines())


# with open('some.txt', 'w') as f:
#     f.write()


# with open('some.txt', 'a') as f:
#     f.write('\nkkk')


# with open('some2.txt', 'w') as f:
#     f.write('A')
#     f.write('K')



# with open('some3.txt', 'a') as f:
#     f.write('A')
#     f.write('K')


# names = ['Arsen', 'Levon', 'Shavarsh', 'Hermine', 'Astghik']

# with open('new_file.txt', 'w') as f:
#     for i in names:
#         f.write(f'{i}\n')


# with open('new_file.txt', 'r') as f:
#     print(f.read())



# count = 0
# with open('new_file.txt', 'r') as f:
#     for letter in f.read():
#         if letter.isdigit():
#             count += 1
# print(count)


# with open('new_file.txt', 'r') as f:
#     content = f.read().replace(',', '').replace('.', '').split()
# print(max(content, key=len))


