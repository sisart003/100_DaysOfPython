# 6 Modules
# def fib(n):                 # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):                # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# import fibo
# fibo.fib(1000)
# fibo.fib2(100)
# fibo.__name__
# fib = fibo.fib
# fib(500)

# 6.1 More on Modules
# from fibo import fib, fib2
# print(fib(200))
# from fibo import *
# import fibo as fib
# from fibo import fib as fibonacci

# 6.1.1 Executing modules as scripts
# if __name__=="__main__":
#     import sys
#     fib(int(sys.argv[1]))

# 6.1.2 The Module Search Path
# 6.1.3 "Compiled" Python files

# 6.2 Standard Modules
# import sys
# sys.path.append('/ufs/guido/lib/python')

# 6.3 The dir() Function
# import fibo, sys, builtins
# print(dir(fibo))
# print(dir(sys))
# a = [1, 2, 3, 4, 5]
# fib = fibo.fib
# print(dir())
# print(dir(builtins))

# 6.4 Packages

# sound/                                Top-level package
#         __init__.py                   Initialize the sound package
#         formats/                      Subpackage for file formate conversions
#                     __init__.py
#                     wavread.py
#                     wavwrite.py
#                     aiffread.py
#                     aiffwrite.py
#                     auread.py
#                     auwrite.py
#                     ...
#         effects/                      Subpackage for sound effects
#                     __init__.py
#                     echo.py
#                     surround.py
#                     reverse.py
#                     ...
#         filters/                      Subpackage for filters
#                     __init__.py
#                     equalizer.py
#                     vocoder.py
#                     karaoke.py
#                     ...

# import sound.effects.echo
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# from sound.effects import echo
# echo.echofilter(input, output, delay=0.7, atten=4)

# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)

# 6.4.1 Importing * From a Package
# __all__ = ['echo', 'surround', 'reverse']
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

# 6.4.2 Intra-package References
# from . import echo
# from .. import formates
# from ..filters import equalizer

# 6.4.3 Packages in Multiple Directories