# import time
# list_ = [1, 1, 1, 2, 3, 3, 4, 4, 2, 2]
# def one_element(result):
#     def  consecutive_groups(mylist, count=1):
#         if len(mylist) == 1:
#             return [count]
#         elif mylist[0] == mylist[1]:
#             return consecutive_groups(mylist[1:], count + 1)
#         else:
#             return [count] + consecutive_groups(mylist[1:], count=1)
#     if len(result) == 1:
#         return result
#     else:
#         step_result = consecutive_groups(result)
#         print(result, step_result)
#         time.sleep(1.5)
#         return one_element(step_result)
# print(one_element(list_))