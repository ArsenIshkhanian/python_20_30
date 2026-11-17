# class Library:
#     def __init__(self, name, books=[], borrow_books=[]):
#         self.name = name
#         self.books = books
#         self.borrow_books = borrow_books

#     def add_book(self, name):
#         if name in self.books:
#             print(f'The <{name}> book already in {self.name} library!')
#         else:
#             self.books.append(name)

#     def remove_book(self, name):
#         if name in self.books:
#             self.books.remove(name)
#         else:
#             print(f'The <{name}> book not in {self.name} library!')

#     def borrow_book(self, name):
#         if name in self.books:
#             self.books.remove(name)
#             self.borrow_books.append(name)
#         else:
#             print(f'The <{name}> book not found in {self.name} library for borrow!')

#     def return_book(self, name):
#         if name in self.borrow_books:
#             self.borrow_books.remove(name)
#             self.books.append(name)
#         else:
#             print(f'The <{name}> book, not found in borrows book!')

#     def available_books(self):
#         print("-------------These are Avaliable books for now-------------")
#         for book in self.books:
#             print(book)

#     def show_borrow_books(self):
#         print("-------------These are borrow books for now-------------")
#         for book in self.borrow_books:
#             print(book)


# books = [
#     "Harry Potter",
#     "The Great Gatsby",
#     "1984",
#     "Animal Farm",
# ]

# library_1 = Library('Ազգային գրադարան', books)
# # library_1.available_books()
# library_1.add_book('Մեր թաղը')
# library_1.add_book('Սամվել')
# library_1.add_book('Ես եւ նա')
# library_1.borrow_book('Harry Potter')
# library_1.borrow_book('Animal Farm')
# library_1.return_book('Մեր թաղը')
# library_1.available_books()
# library_1.show_borrow_books()


# class Employer:
#     def __init__(self, idt, name, surname, salary):
#         self.idt = idt
#         self.name = name
#         self.surname = surname
#         self.salary = salary

#     def get_salary(self):
#         return self.salary

#     def upgrade_salary(self, percent):
#         self.salary *= (1 + (percent / 100))
#         self.salary = int(self.salary)

#     def get_info(self):
#         return f'Name -> {self.name}\nSurname -> {self.surname}\nSalary -> ${self.salary}'

# class Programmer(Employer):
#     def __init__(self,idt, name, surname, salary, cp_type):
#         super().__init__(idt, name, surname, salary)
#         self.cp_type = cp_type

#     def get_cp(self):
#         return self.cp_type

#     def upgrade_salary(self, percent):
#         self.salary *= (1 + ((percent + 2) / 100))
#         self.salary = int(self.salary)

# class Stom(Employer):
#     def __init__(self, idt, name, surname, salary, deadline, license=False):
#         super().__init__(idt, name, surname, salary)
#         self.deadline = deadline
#         self.license = license

#     def check_lisence(self):
#         return self.license

#     def check_deadline(self):
#         return self.deadline

#     def pass_day(self):
#         self.deadline -= 1

# class Company:
#     def __init__(self, name, employers=[]):
#         self.name = name
#         self.employers = employers

#     def add_employer(self, employer):
#         self.employers.append(employer)

#     def show_employer(self, idt):
#         for employer in self.employers:
#             if employer.idt == idt:
#                 return employer

#     def termination(self, idt):
#         for employer in self.employers:
#             if employer.idt == idt:
#                 self.employers.remove(employer)

#     def show_all_employers(self):
#         for employer in self.employers:
#             print(employer.get_info())
    
# employee_1 = Programmer(1, 'Arsen', 'Ishkhanian', 200000, 'Macbook M3 Pro')
# employee_2 = Stom(2, 'Astghik', 'Arabyan', 450000, 90)
# Techlam = Company('TechLam')
# Techlam.add_employer(employee_1)
# Techlam.add_employer(employee_2)

# print(employee_1.get_salary())
# employee_1.upgrade_salary(10)
# print(f'New salary is -> {employee_1.salary}')
# print(employee_2.get_salary())
# employee_2.upgrade_salary(-55)
# print(f'New salary is -> {employee_2.salary}')

# vat_ashxatox_1 = Techlam.show_employer(2)
# print('\n')
# print(vat_ashxatox_1.get_info())
# vat_ashxatox_1.upgrade_salary(100)
# print('\nUpgrade Salary!!!\n')
# print(vat_ashxatox_1.get_info())
# Techlam.termination(2)
# print('\nAfter Termination')
# Techlam.show_all_employers()


# import random
# class Fight:
#     def __init__(self, username, health=100):
#         self.username = username
#         self.health = health

#     def attack(self, other):
#         damage = random.randint(1, 20)
#         other.health -= damage

# user_1 = Fight('Arsen_08')
# user_2 = Fight('Levon_500')

# while user_1.health > 0 and user_2.health > 0:
#     choice = random.randint(1, 2)
#     if choice == 1:
#         user_1.attack(user_2)
#     else:
#         user_2.attack(user_1)

# if user_1.health <= 0:
#     print(f'{user_2.username} WIN!!!')
# else:
#     print(f'{user_1.username} WIN!!!')


