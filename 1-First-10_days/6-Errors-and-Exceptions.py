# 8 Errors and Exceptions

# 8.1 Syntax Errors
# while True print('Hello World')   # cause syntax error

# 8.2 Exceptions
# print(10 * (1/0))     # ZeroDivisionError
# print(4 + spam*3)     # NameError
# print('2' + 2)        # TypeError

# 8.3 Handling Exceptions
# while True:
#     try:
#         x = int(input('Please enter a number: '))
#         break
#     except ValueError:
#         print('Oops! That was no valid number. Try again...')

# class B(Exception):
#     pass
# class C(B):
#     pass
# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print('D')
#     except C:
#         print('C')
#     except B:
#         print('B')

import sys
# try:
#     f = open('sample.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("Os error: {0}".format(err))
# except ValueError:
#     print('Could not convert data to an integer.')
# except BaseException as err:
#     print(f'Unexpected {err=}, {type(err)=}')
#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))       # the exception instance
#     print(inst.args)        # arguments stored in .args
#     print(inst)             # __str__ allows args to be printed directly,
#                             # but may be overridden in exception subclasses
#     x, y = inst.args        # unpack args
#     print('x =', x)
#     print('y =', y)

# def this_fails():
#     x = 1/0

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# 8.4 Raising Exceptions
# raise NameError('HiThere')  # NameError: HiThere

# raise ValueError # shothand for 'raise ValueError()'
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An excpetion flew by!')
#     raise

# 8.5 Exception Chaining
# raise RuntimeError from exc # exc be exception instance or None.

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None

# 8.6 User-defined Exceptoins
# 8.7 Defining Clean-up Actions
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
# print(bool_return())

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print('division by zero!')
#     else:
#         print('result is', result)
#     finally:
#         print('executing finally clause')
# print(divide(2, 1))
# print(divide(2, 0))
# print(divide('2', '1'))

# 8.8 Predefined Clean-up Actions
# for line in open('sample.txt'):
#     print(line, end='')

# with open('sample.txt') as f:
#     for line in f:
#         print(line, end='')