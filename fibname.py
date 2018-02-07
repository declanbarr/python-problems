# Declan Barr 07 Feb 2018
# I put my surname Barr into the fibname.py program. It returned the following "The first letter B is number 66
# The last letter r is number 114" The ASCII decimal numbers for B and r are 66 and 114, respectively. Therefore, the ord function appears to return the ASCII decimal value for the character. On googling the ord function I found this "The ord() method returns an integer representing Unicode code point for the given Unicode character." (https://www.programiz.com/python-programming/methods/built-in/ord)
#
# The output of the program was:
#
# My surname is Barr
# The first letter B is number 66
# The last letter r is number 114
# Fibonacci number 180 is 18547707689471986212190138521399707760
# Adapted from https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Barr"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
