# list_ = [1, 2, 3, 4, 5, 6]

# def summ(mylist):
#     if mylist == []:
#         return 0
#     else:
#         return mylist[0] + summ(mylist[1:]) 

# print(summ(list_))

# 'Python' -> 'nohtyP'

#---------------------------------------------------------------------

# def reverse(text):
#     if text == '':
#         return ''
#     else:
#         return text[-1]  + reverse(text[:-1])

    # n + reverse(Pytho)
    # n + o + reverse(Pyth)
    # n + o + h + reverse(Pyt)
    # n + o + h + t + reverse(Py)
    # n + o + h + t + y + reverse(P)
    # n + o + h + t + y + P + reverse()
    # n + o + h + t + y + P + ''

# print(reverse('Python'))

#---------------------------------------------------------------------

# def reverse(text):
#     if text == '':
#         return ''
#     else:
#         return reverse(text[1:]) + text[0]

#     # reverse(ello) + H
#     # reverse(llo) + e + H
#     # reverse(lo) + l + e + H
#     # reverse(o) + l + l + e + H
#     # reverse() + o + l + l + e + H
#     # '' + o + l + l + e + H

# print(reverse('Hello'))

#---------------------------------------------------------------------

# def count(number):
#     if number == 0:
#         return 0
#     else:
#         return 1 + count(number//10)
#     # 1 + count(125)
#     # 1 + 1 + count(12)
#     # 1 + 1 + 1 + count(1)
#     # 1 + 1 + 1 + 1 + count(0)
#     # 1 + 1 + 1 + 1 + 0

# print(count(1254))

#---------------------------------------------------------------------

# def power(tiv, astichan):
#     if astichan == 0:
#         return 1
#     else:
#         return tiv * power(tiv, astichan - 1)

#     # 3 * power(3, 3)
#     # 3 * 3 * power(3, 2)
#     # 3 * 3 * 3 * power(3, 1)
#     # 3 * 3 * 3 * 3 * power(3, 0)
#     # 3 * 3 * 3 * 3 * 1
# print(power(3, 4))


#---------------------------------------------------------------------


# text = 'level'
# def palindrome(text):
#     if text == '' or len(text) == 1:
#         return True
#     elif text[0] == text[-1]:
#         return palindrome(text[1:-1])
#     else:
#         return False

#     # palindrome(eve)
#     # palindrome(v)
#     # True
# print(palindrome(text))


#---------------------------------------------------------------------


# def finder(mylist, target, index=0):
#     if mylist == []:
#         return -1
#     elif mylist[0] == target:
#         return index
#     else:
#         return finder(mylist[1:], target, index + 1)

# list_ = [4, 7, 4, 5, 2, 3, 1]
# print(finder(list_, 3))


#---------------------------------------------------------------------


# def reducing(text):
#     if len(text) == 1:
#         return text[0]
#     elif text[0] == text[1]:
#         return reducing(text[1:])
#     else:
#         return text[0] + reducing(text[1:])

# print(reducing('aaaaabbbbbccccccc'))