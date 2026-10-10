# list_ = ['A', 12, 'B', 4, 'A', 3, 'C', 1] 


# def decoding(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + decoding(mylist[2:])

#     #['A'] * 12 + decoding(['B', 4, 'A', 3, 'C', 1])
#     #['A'] * 12 + ['B'] * 4 + decoding(['A', 3, 'C', 1])
#     #['A'] * 12 + ['B'] * 4 + ['A'] * 3 + decoding(['C', 1])
#     #['A'] * 12 + ['B'] * 4 + ['A'] * 3 + ['C'] * 1 + []


# print(decoding(list_))




# list_ = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A']


# def encoding(mylist, count=1):
#     if mylist == []:
#         return []
#     elif len(mylist) > 1 and mylist[0] == mylist[1]:
#         return encoding(mylist[1:], count=count + 1)
#     else:
#         return [mylist[0], count] + encoding(mylist[1:], count=1)

# print(encoding(list_))




# nato = {
#     'A': 'Alpha',
#     'B': 'Bravo',
#     'C': 'Charlie',
#     'D': 'Delta',
#     'E': 'Echo',
#     'F': 'Foxtrot',
#     'G': 'Golf',
#     'H': 'Hotel',
#     'I': 'India',
#     'J': 'Juliet',
#     'K': 'Kilo',
#     'L': 'Lima',
#     'M': 'Mike',
#     'N': 'November',
#     'O': 'Oscar',
#     'P': 'Papa',
#     'Q': 'Quebec',
#     'R': 'Romeo',
#     'S': 'Sierra',
#     'T': 'Tango',
#     'U': 'Uniform',
#     'V': 'Victor',
#     'W': 'Whiskey',
#     'X': 'Xray',
#     'Y': 'Yankee',
#     'Z': 'Zulu'
# }



# def decoding(text):
#     if text == '':
#         return ''
#     else:
#         return nato[text[0]] + ' ' + decoding(text[1:])
    
# text = input("Text: ").upper() #Hello
# print(decoding(text))



# roman = {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }

# def roman_to_numb(number):
#     if number == '':
#         return 0
#     elif len(number) > 1 and roman[number[1]] > roman[number[0]]:
#         return (roman[number[1]] - roman[number[0]]) + roman_to_numb(number[2:])
#     else:
#         return roman[number[0]] + roman_to_numb(number[1:])

# number = input("Roman: ")
# print(roman_to_numb(number))



# list_ = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

# def decoding(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == list:
#         return decoding(mylist[0]) + decoding(mylist[1:])
#     else:
#         return [mylist[0]] + decoding(mylist[1:])
    
# print(decoding(list_))

