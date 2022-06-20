# 10 Brief Tour of the Standard Library

# 10.1 Operating System Interface
import os, shutil, glob, sys, argparse, re, math, random, statistics, smtplib, zlib
# print(os.getcwd())                        # Return the current working directoy
# print(os.chdir('/server/accesslogs'))     # Change current working directoy
# print(os.system('mkdir today'))           # Run the command mkdir in the system shell

# print(dir(os))
# print(help(os))
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

# 10.2 File Wildcards
# print(glob.glob('*.py'))

# 10.3 Command Line Arguments
# print(sys.argv)
# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top liens from each file')
# parser.add_argument('sample.txt', nargs='+')
# parser.add_argument('-1', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# 10.4 Error Output Redirection and Program Termination
# print(sys.stderr.write('Warning, log file not found starting a new one\n'))

# 10.5 String Pattern Matching
# print(re.findall(r'\bf[a-]*', 'which foot or hand fell fastest'))
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# print('tea for too'.replace('too', 'two'))

# 10.6 Mathematics
# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))                # Sampling without replacement
# print(random.random())                              # random float
# print(random.randrange(6))                          # random integer chosen from range(6)

# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# 10.7 Internet Access
# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()                # Convert bytes to a str
#         if line.startswith('datetime'):
#             print(line.rstrip())            # Remove trailing newline

# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'toyang.1996@gmail.com')
# print("""
#     To: Sisart
#     From: Toyang

#     Hello, How are you?
# """)
# server.quit()

# 10.8 Dates and times

# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))

# # dates support calenday arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)

# 10.9 Data compression
# s = b'witch which has which witches wrist watch'
# print(len(s))

# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))

# 10.10 Performance Measurement
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 10.11 Quality Control
# def average(values):
#     """Computes the arithmetic mean of a list of numbers/
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)

# import doctest
# doctest.testmod()       # automatically validate the embedded tests

# import unittest
# class TestStatisticalFUnctions(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
# unittest.main()         # Calling from the command line invokes all tests

# 10.12 Batteries Included