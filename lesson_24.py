# import time
# def encoder(mylist, new_list=[], count=1):
#     time.sleep(0.5)
#     print(mylist, new_list)
#     if len(mylist) == 1 and new_list == []:
#         return [count]
#     elif len(mylist) == 1:
#         return encoder(new_list + [count])
#     elif mylist[0] == mylist[1]:
#         return encoder(mylist[1:], new_list, count + 1)
#     else:
#         return encoder(mylist[1:], new_list + [count])

# list_ = [1, 1, 1, 2, 2, 4, 5, 6, 6]
# print(encoder(list_))



# def solver(coin, amount):
#     if coin == 0 or amount == 0:
#         return coin == amount
#     else:
#         return solver(coin - 1, amount - 25) or solver(coin - 1, amount - 10) or solver(coin - 1, amount - 5) or solver(coin - 1, amount - 1)


# print(solver(5, 59))