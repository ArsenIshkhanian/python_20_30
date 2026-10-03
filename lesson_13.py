# list_ = []
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1)
# list_.append(1) # O(n)
# list_.append(1)


# list_ = [5, 2, 3, 4, 5, 6]
# for i in list_:
#     if i == 5:
#         print(i)
#         break


# import random
# comp = random.randint(1, 100)
# for i in range(1, 101):
#     if i == comp:
#         print(i)
#         break


# n = 4
# for i in range(n):
#     for j in range(n):
#         print()


# nums = [4, 6, 7, 3, 2, 2]
# nums.sort() # n log2n

# for i in nums:
#     if nums.count(i) > 1:
#         print(i)
#         break

# count = 0
# for i in nums:
#     if i == 4:
#         count += 1

# print(count)

# nums = [4, 6, 7, 3, 2, 2]
# nums.sort() # n log2n
# # print(nums)

# for i in range(len(nums) - 1): # O(n)
#     if nums[i] == nums[i + 1]:
#         print(nums[i])
#         break
# else:
#     print("Chka tenc tiv")



# nums = [1, 3, 4, 6, 8, 10]
# target = 14
# status = False

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])
#             status = True
#             break
#     if status == True:
#         break


# nums = [1, 3, 4, 6, 8, 10]
# target = 14
# i = 0
# j = len(nums) - 1
# while i < j:
#     if nums[i] + nums[j] < target:
#         i += 1
#     elif nums[i] + nums[j] > target:
#         j += 1
#     else:
#         print(nums[i], nums[j])
#         break


# nums = [4, 8, 2, 10, 6]
# maximum = 0

# for value in nums:
#     if value > maximum:
#         maximum = value

# print(maximum)

# nums = [4, 9, 2, 9, 7]
# nax = 0
# maximum = 0
# for value in nums:
#     if value > maximum:
#         nax = maximum
#         maximum = value
#     elif value > nax and value != maximum:
#         nax = value
# print(nax)
