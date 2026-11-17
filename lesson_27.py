###ALGORITHMS
# def linear_search(array, target): #->O(n)
#     for element in array:
#         if element == target:
#             return True
#     return False


# mylist = [1, 7, 4, 5, 3, 2, 8, 9, 10]
# target = 7
# print(linear_search(mylist, target))


#array should be sorted!!!!
# def binary_search(array, target): #Log(n)
#     while array:
#         middle = len(array)// 2#5
#         print(array)
#         if array[middle] == target:
#             return True
#         elif array[middle] > target:
#             array = array[:middle]
#         else:
#             array = array[middle + 1:]
#     return -1


# mylist = [1, 4, 5, 7, 10, 12, 15, 25, 35, 67, 101]
# target = 13
# print(binary_search(mylist, target))



#SORT 
# def bubble_sort(mylist): #BEST CASE O(n) -> Av O(n**2)
#     for i in range(len(mylist)):
#         status = True
#         for j in range(len(mylist) - 1 - i):
#             if mylist[j] > mylist[j + 1]:
#                 mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
#                 status = False
#         if status:
#             return mylist

#     return mylist

# sorted_list = bubble_sort([1, 2, 3, 4, 5])
# print(sorted_list)


# def selection_sort(mylist): #O(n**2)
#     for i in range(len(mylist)): # 0
#         minimum = mylist[i] # 1
#         minimum_index = i # 3
#         for j in range(i + 1, len(mylist)):#2
#             if mylist[j] < minimum:
#                 minimum = mylist[j]
#                 minimum_index = j
#         mylist[i], mylist[minimum_index] = mylist[minimum_index], mylist[i]
#     return mylist
# sorted_list = selection_sort([1, 2, 3, 4, 5])
# print(sorted_list)



# def insertion_sort(mylist):#O(n**2)
#     for i in range(1, len(mylist)):
#         key = mylist[i - 1] 
#         j = i 
#         while j > 0 and mylist[j] < key:
#             mylist[j - 1], mylist[j] = mylist[j], mylist[j - 1]
#             j -= 1
#             key = mylist[j - 1] 
#     return mylist
# sorted_list = insertion_sort([2, 3, 5, 1, 4, 5]) #[2, 3, 1, 5, 4] -> [2, 1, 3, 5, 4] -> [1, 2, 3, 4, 5]
# print(sorted_list)


# def merge_sort(array): #O(nlogn)
#     if len(array) == 1:
#         return array

#     middle = len(array) // 2
#     left = merge_sort(array[:middle]) # [2, 3, 5]
#     right = merge_sort(array[middle:]) # [1, 4, 7]
#     i = 3
#     j = 2
#     new_list = [] 
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             new_list.append(left[i])
#             i += 1
#         elif left[i] > right[j]:
#             new_list.append(right[j])
#             j += 1

#     new_list.extend(left[i:])
#     new_list.extend(right[j:])

#     return new_list

# sorted_list = merge_sort([2, 3, 5, 1, 4, 7])
# print(sorted_list)


###QUCIK SORT -> nlog(n)
# def median_tree(a, b, c):
#     maximum = max(a, b, c)
#     minimum = min(a, b, c)
#     return (a + b + c) - minimum - maximum


# def quick_sort(array):
#     if len(array) == 1:
#         return array
    
#     pivot = median_tree(array[0], array[len(array) // 2], array[-1])

#     poqr = [i for i in array if i < pivot] #[0]
#     havasar = [i for i in array if i == pivot] #[1]
#     mets = [i for i in array if i > pivot] #[2, 3, 5, 4, 7]

#     return quick_sort(poqr) + havasar + quick_sort(mets)
#     #[0] + [1] + quick_sort([2, 3, 5, 4, 7])
#     #[0] + [1] + qucik_sort([2, 3, 4]) + [5] + quick_sort([7])
#     #[0] + [1] + qucik_sort([2, 3, 4]) + [5] + [7]
#     #[0] + [1] + [2] + [3] + [4] + [5] + [7]
#     #[0, 1, 2, 3, 4, 5, 7
# sorted_list = quick_sort([2, 3, 5, 1, 4, 7, 0])
# print(sorted_list)