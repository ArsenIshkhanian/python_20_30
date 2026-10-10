# def factorial(n):
#     if n == 1:
#         return 10
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))



# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 2) + fibonacci(n - 1)
    # fib(4) + fib(5)
    # fib(2) + fib(3) + fib(5)
    # fib(0) + fib(1) + fib(3) + fib(5)
    # 0 + 1 + fib(3) + fib(5)
    # 0 + 1 + fib(1) + fib(2) + fib(5)
    # 0 + 1 + 1 + fib(2) + fib(5)
    # 0 + 1 + 1 + fib(2) + fib(5)
    # 0 + 1 + 1 + fib(0) + fib(1) + fib(5)
    # 0 + 1 + 1 + 0 + 1 + fib(5)
    # 0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
    # 0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
    # 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
    # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
    # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
    # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
    # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
    # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8

# print(fibonacci(6))



# list_ = [1, 8, 7, 3, 4, 5, 2, 9]
# print(list_[1:])
# list_ = list_[1:]
# print(list_[1:])



# def sum_of_element(mylist):
#     if mylist == []:
#         return 0
#     else:
#         return mylist[0] + sum_of_element(mylist[1:])
    
# print(sum_of_element(list_))


# x = [1, 2, 3]
# x.remove(2)
# x.pop(1)
# del x[0]
# y = []
# x = x + y
# print(x)


# elements = [1, 6, 7, 4, 2, 3, 0, 9]


# def filter_even(elements):
#     if elements == []:
#         return []
#     elif elements[0] % 2 == 0:
#         return [elements[0]] + filter_even(elements[1:])
#     else:
#         return filter_even(elements[1:])
    #[6, 7, 4, 2, 3, 0, 9]
    #[6] + [7, 4, 2, 3, 0, 9]
    #[6] + [4, 2, 3, 0, 9]
    #[6] + [4] + [2, 3, 0, 9]
    #[6] + [4] + [2] + [3, 0, 9]
    #[6] + [4] + [2] + [0, 9]
    #[6] + [4] + [2] + [0] [9]
    #[6] + [4] + [2] + [0] + []

# print(filter_even(elements))



# def encode(mylist):
#     pass

# print(encode(["A", 12, "B", 4, "A", 6, "B", 1, "C", 5]))
# ["A","A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
# "B", "B", "A", "A", "A", "A", "A", "A", "B"]


# list_ = ['A', 12, 'B', 4, 'A', 6, 'B', 1, 'C', 5]
# def x(mylist):
#     if mylist == []:
#         return []
#     char = mylist[0]
#     digit = mylist[1]
#     return [char] * digit + x(mylist[2:])

# print(x(list_))



# ["A","A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
# "B", "B", "A", "A", "A", "A", "A", "A", "B"]
# ["A", 12, "B", 4, "A", 6, "B", 1]


# list_ = ['A', 12, 'B', 4, 'A', 6, 'B', 1, 'C', 5]
# def x(mylist):
#     if mylist == []:
#         return []
#     char = mylist[0]
#     digit = mylist[1]
#     return [char] * digit + x(mylist[2:])

# print(x(list_))