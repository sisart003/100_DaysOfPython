# 9 Classes
# 9.1 A Word About Names and Objects
# 9.2 Python Scopes and Namespaces
# 9.2.1 Scrops and Namespaces Example
# def scope_test():
#     def do_local():
#         spam = 'local spam'
#     def do_nonlocal():
#         nonlocal spam
#         spam = 'nonlocal spam'
#     def do_global():
#         global spam
#         spam = 'global spam'
    
#     spam = 'test spam'
#     do_local()
#     print('After local assignment: ', spam)
#     do_nonlocal()
#     print('After nonlocal assignment: ', spam)
#     do_global()
#     print('After global assignment: ', spam)

# scope_test()
# print('In global scope: ', spam)

# 9.3 A First Look at Classes
# 9.3.1 Class Definition Syntax
# class ClassnName:
#     <statement-1>
#     <statement-N>

# 9.3.2 Class Objects
# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'

# x = MyClass()

# def __init__(self):
#     self.data = []

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)

# print(x. r, x.i)

# 9.3.3 Instance Objects
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter

# 9.3.4 Method Objects
# x.f()
# xf = x.f
# while True:
#     print(xf())

# 9.3.5 Class and Instance Variables
# class Dog:
#     kind = 'canine'             # class variable shared by all instances

#     def __init__(self, name):
#         self.name = name        # instance variable unique to each instance

# d = Dog('Fido')
# c = Dog('Buddy')
# print(d.kind)                   # shared by all dogs
# print(c.kind)                   # shared by all dogs
# print(d.name)                   # unique to d
# print(c.name)                   # unique to c

# class Dog:
#     tricks = []

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.add_trick('roll over'))
# print(e.add_trick('play dead'))
# print(d.tricks)

# much better code
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []        # creates a new empty list for each dog
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)
# print(e.tricks)

# 9.4 Random Remarks
# class Warehouse:
#     purpose = 'storage'
#     region = 'west'
# w1 = Warehouse()
# print(w1.purpose, w1.region)
# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)

# Function defined outside the  class
# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'
    
#     h = g

# class Bag:
#     def __init__(self):
#         self.data = []
    
#     def add(self, x):
#         self.data.append(x)
    
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

# 9.5 Inheritance
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     <statement-N>
# class DerivedClassName(modename.BaseClassName):

# 9.5.1 Multiple Inheritance
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     <statement-N>

# 9.6 Private Variables
# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
    
#     __update = update # private copy of original update() method

# class MappingSubclass(Mapping):
#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# 9.7 Odds and Ends
# class Employee:
#     pass

# john = Employee()       #Create an empty employee record
# # fill the fields of the record
# john.name = 'John Doe'
# john.dept = 'Computer lab'
# john.salary = 1000

# 9.8 Iterators
# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one': 1, 'two': 2}:
#     print(key)
# for char in '123':
#     print(char)
# for line in open('sample.txt'):
#     print(line, end='')

# s = 'abc'
# it = iter(s)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))

# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# rev = Reverse('spam')
# print(iter(rev))
# for char in rev:
#     print(char)

# 9.9 Generators
# def reverse(data):
#     for index in range(len(data) -1, -1, -1):
#         yield data[index]

# for char in reverse('golf'):
#     print(char)

# 9.10 Generator Expressions
# print(sum(i*i for i in range(10)))      # sum of squares
# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# print(sum(x*y for x,y in zip(xvec, yvec)))
# unique_words = set(word for line in page for word in line.split())
# valedictorian = max((student.gpa, student.name) for student in graduates)
# data = 'goolf'
# list(data[i] for i in range(len(data)-1, -1, -1))