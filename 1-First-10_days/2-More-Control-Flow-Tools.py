# 4 More Control Flow Tools

# 4.1 If Statement
# x = int(input('Please enter an integer: '))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# 4.2 For Statement
# measure some strings:
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# Strategy: Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(user, status)

# 4.3 The range() Function
# for i in range(5):
#     print(i)

# print(list(range(5, 10)))
# print(list(range(0, 10, 3)))
# print(list(range(-10, -100, -30)))

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# print(range(10))
# print(sum(range(4)))    # 0 + 1 + 2 + 3

# 4.4 break and continue Statements, and else Clauses on Loops
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # Loop fell through without finding a factor
#         print(n, ' is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print('Found an even number', num)
#         continue
#     print('Found an odd number', num)

# 4.5 pass statements
# while True:
#     pass # Busy-wait for keyboard interrupt (Ctrl+C)

# class MyEmptyClass:
#     pass

# def initlog(*args):
#     pass # Remember to implement this!

# 4.6 match Statements
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case 401 | 403 | 404:
#             return "Not allowed"
#         case _:
#             return "Something's wrong with the internet"


# point is an (x, y) tuple
# class Point:
#     x : int
#     y : int

# def where_is(point):
#     match point:
#         case(0 ,0):
#             print('Origin')
#         case(0, y):
#             print(f"Y={y}")
#         case(x, 0):
#             print(f"X={x}")
#         case(x, y):
#             print(f"X={x}, Y={y}")
#         case _:
#             raise ValueError("Not a Point")

# Point(1, var)
# Point(1, y=var)
# Point(x=1, y=var)
# Point(y=var, x=1)

# 4.7 Defining Functions
# def fib(n):     # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         # print(a, end=' ')
#         result.append(a)
#         a, b = b, a+b
#     # print()
#     return result



# f = fib(100)
# print(f)
# print(fib)

# 4.8 More on Defining Function
# 4.8.1 Default Argument Values
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# print(i)

# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# 4.8.2 Keyword Arguments
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, " volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
    
# print(parrot(1000))                                         # 1 positional argument
# print(parrot(voltage=1000))                                 # 1 keyword argument
# print(parrot(voltage=1000000, action='VOOOOOOM'))           # 2 keyword arguments
# print(parrot(action='VOOOOOOOOM', voltage=1000000))         # 2 keyword arguments
# print(parrot('a million', 'bereft of life', 'jump'))        # 3 positional arguments
# print(parrot('a thousand', state='pushing up the daisies')) # 1 positional, 1 keyword

# parrot()                        # required argument missing
# parrot(voltage=5.0, 'dead')     # non-keyword argument after a keyword argument
# parrot(110, voltage=220)        # duplicate value for the same argument
# parrot(actor='John Cleese')     # unknown keyword argument

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print('-' * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#             "It's really very, VERY runny, sir.",
#             shopkeeper='Michael Palin',
#             client="John Cleese",
#             sketch="Cheese Shop Sketch")

# 4.8.3     Special parameters
# 4.8.3.1   Positional-or-Keyword Arguments
# 4.8.3.2   Positional-Only Parameters
# 4.8.3.3   Keyword-Only Arguments
# 4.8.3.4   Function Examples
# def standard_arg(arg):
#     print(arg)
# def pos_only_arg(arg, /):
#     print(arg)
# def kwd_only_arg(*, arg):
#     print(arg)
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)

# standard_arg(2)
# standard_arg(arg=2)

# pos_only_arg(1)
# pos_only_arg(arg=2)

# kwd_only_arg(3)
# kwd_only_arg(arg=3)

# combined_example(1, 2, 3)
# combined_example(1, 2, kwd_only=3)
# combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)

# def foo(name, **kwds):
#     return 'name' in kwds
# foo(1, **{'name': 2})

# def foo(name, /, **kwds):
#     return 'name' in kwds
# foo(1, **{'name': 2})

# 4.8.3.5 Recap
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     pass

# 4.8.4 Arbitrary Argument Lists
# def write_multiple_items(file, separator, * args):
#     file.write(separator.join(args))
# def concat(*args, sep="/"):
#     return sep.join(args)
# concat("earth", "mars", "venus")
# concat('earth', 'mars', 'venus', sep='.')

# 4.8.5 Unpacking Argument Lists
# list(range(3, 6))   # normal call with separate arguments

# args = [3, 6]
# list(range(*args))  # call with arguments unpacked from a list

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
# d = {"voltage":"four million", "state":"bleedin' demised", "action":"VOOM"}
# parrot(**d)

# 4.8.6 Lambda Expressions
# def make_incrementor(n):
#     return lambda x: x + n
# f = make_incrementor(42)
# print(f(0))
# print(f(1))

# pairs = [(1, 'one'), (2, 'two'), (2, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# 4.8.7 Documentation Strings
# def my_function():
#     """Do nothing, but document it
    
#     No, really, it doesn't do anyting.
#     """
#     pass
# print(my_function.__doc__)

# 4.8.8 Function Annotation
# def f(ham: str, eggs: str='eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
# print(f('spam'))