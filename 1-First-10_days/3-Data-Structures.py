# 5 Data Structures

# 5.1 More on Lists
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))
# print(fruits.count('tangerine'))
# print(fruits.index('banana'))
# print(fruits.index('banana', 4)) # Find next bnana starting a position 4
# fruits.reverse()
# print(fruits)
# fruits.sort()
# print(fruits)
# print(fruits.pop())

# 5.1.1 Using Lists as Stacks
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# print(stack.pop())

# 5.1.2 Using Lists as Queues
# from collections import deque
# queue = deque(['Eric', 'John', 'Michael'])  # Terry arrives
# queue.append('Terry')                       # Graham arrives
# queue.append('Graham')                      # The first to arrive now leaves
# queue.popleft()                             # The second to arrive now leaves
# queue.popleft()                             # Remaining queue in order of arrival
# print(queue)

# 5.1.3 List Comprehensions
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

# squares = [x**2 for x in range(10)]
# print(squares)

# a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(a)

# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# vec = [-4, -2, 0, 2, 4]
# [x*2 for x in vec]                              # create a new list with the values doubled
# [x for x in vec if x >= 0]                      # filter the list to exclude negative numbers
# [abs(x) for x in vec]                           # apply a function to all the elements
# freshfruit = ['    banana', '   loganberry ', 'passion fruit    ']
# [weapon.strip() for weapon in freshfruit]       # call a method on each element
# [(x, x**2) for x in range(6)]                   # create a list of 2-tuples like (number, square)
# [x, x**2 for x in range(6)]                     # the tuple must be parenthesized, otherwise an error is raised
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([num for elem in vec for num in elem])

# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])

# 5.1.4 Nested List Comprehensions
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print([[row[i] for row in matrix] for i in range(4)])

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# print(list(zip(*matrix)))

# 5.2 The del statement
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# del a[2:4]
# del a[:]
# print(a)

# 5.3 Tuples and Sequences
# t = 12345, 54321, 'hello!'
# print(t[0])
# print(t)
# u = t, (1, 2, 3, 4, 5)      # Tuples may be nested
# print(u)
# t[0] = 8888                 # Tuples are immutable
# v = ([1, 2, 3], [3, 2, 1])  # but they can contain mutable objects
# print(v)

# empty = ()
# singleton = 'hello',    # <-- note trailing comma
# print(len(empty))
# print(len(singleton))
# print(singleton)

# 5.4 Sets
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)               # show that duplicates have been removed
# print('orange' in basket)   # fast membership testing
# print('crabgrass' in basket)

# # Demonstrate set operations on unique letters from two words
# a = set('abracadabra')
# b = set('alacazam')
# print(a)                    # unique letters in a
# print(a - b)                # letters in a but not in b
# print(a | b)                # letters in a or b or both
# print(a & b)                # letters in a and b
# print(a ^ b)                # letters in a or b but not both

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# 5.5 Dictionaries
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# # print(tel)
# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# print(sorted(tel))
# print('guido' in tel)
# print('jack' not in tel)

# dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {x : x**2 for x in (2, 4, 6)}
# dict(sape=4139, guido=4127, jack=4098)

# 5.6 Looping Techniques
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}.'.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)
# for i in sorted(set(basket)):
#     print(i)

# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)

# 5.7 More on Conditions
# string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)

# 5.8 Comparing Sequences and Other Types
# (1, 2, 3)               < (1, 2, 4)
# [1, 2, 3]               < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal'  < 'Python'
# (1, 2, 3, 4)            < (1, 2, 4)
# (1, 2)                  < (1, 2, -1)
# (1, 2, 3)              == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))    < (1, 2, ('abc', 'a'), 4)