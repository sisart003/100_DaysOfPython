# This is the first comment
# spam = 1 # and this is the second comment
         # ... and now a third!
# text = '# This is not a comment because it\'s inside quotes.'

# Using Python as a Canculator
# Numbers
# print(2 + 2)
# print(50 - 5 * 6)
# print((50 - 5 * 6 ) / 4)
# print(8 / 5)        # division always returns a floating point number
# print(17 / 3)       # classic division returns a float
# print(17 // 3)      # floor division discards the fractional part
# print(17 % 3)       # the % operator reutns the remainder of the division
# print(5 * 3 + 2)    # floored quotient * divisor + remainder
# print(5 ** 2)       # 5 squared
# print(2 ** 7)       # 2 to the power of 7
# width = 20
# height = 5 * 9
# print(width * height)
# print(4 * 3.75 - 1)
# tax = 12.5 / 100
# price = 100.50
# print(price * tax)
# print(price + _)  # I'm confused i think it only run in shell
# print(round(_, 2))# Same goes here

# Strings
# print('spam eggs')                  # single quotes
# print('doesn\'t')                   # use \' to escape the single quote...
# print("doesn't")                    # ...or use double quotes instead
# print('"Yes,\" they said.')
# print("\"Yes,\" they said.")
# print('"Isn\'t," they said.')
# s = 'First line. \nSecond line.'    # \n means newline
# print(s)                            # \n produces a new line
# print('C:\some\name')               # here \n means newline!
# print(r'C:\some\name')              # note the r before the quote
# print("""\
#     Usage:  thingy [OPTIONS]
#             -h                      Display this usage message
#             -H hostname             Hostname to connect to
# """)
# print( 3 * 'un' + 'ium')
# print('Py' 'thon')
# text = ('Put several strings within parentheses '
#         'to have them joined together.')
# print(text)
# prefix = 'Py'
# print(prefix 'thon') # can't concatenate a veriable and a string literal
# print(prefix + 'thon') # if you cant to concatenate variables or a variable and a literal, use +:
# word = 'Python'
# print(word[0])      # character in position 0
# print(word[5])      # character in position 5
# print(word[-1])     # last character
# print(word[-2])     # second-last character
# print(word[-6])

# print(word[0:2])    # characters from position 0 (included) to 2 (excluded)
# print(word[2:5])    # characters from position 2 (included) to 5 (excluded)

# print(word[:2])     # character from the beginning to position 2 (excluded)
# print(word[4:])     # characters from position 4 (included) to the end
# print(word[-2:])    # characters from the second-last (included) to the end
# print(word[:2] + word[2:])
# print(word[:4] + word[4:])
# print('j' + word[1:])
# print(word[:2] + 'py')

# s = 'supercalifragilisticexpialidociuos'
# print(len(s))

# Lists
# squares = [1, 4, 9, 16, 25]
# print(squares)
# print(squares[0])
# print(squares[-1])
# print(squares[-3:])
# print(squares[:])
# print(squares + [36, 49, 64, 81, 100])

# cubes = [1,6, 27, 65, 125]
# print(4 ** 3)           # the cube of 4 is 64, not 65!
# cubes[3] = 64           # replace the wrong value
# print(cubes)
# cubes.append(216)       # add the cube of 6
# cubes.append(7 ** 3)    # and the cube of 7
# print(cubes)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# letters[2:5] = []
# print(letters)
# letters[:] = []
# print(letters)
# letters = ['a', 'b', 'c', 'd']
# print(len(letters))
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)
# print(x[0])
# print(x[0][1])

# Fibonacci series:
# the sum of two elements defines the next
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b

# i = 256*256
# print('The value os i is', i)

# a, b = 0, 1
# while a < 1000:
#     print(a , end=',')
#     a, b = b, a+b