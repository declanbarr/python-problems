# Declan Barr 07 Feb 2018
# My name is Declan, so the first and last letter of my name (D + N = 4 + 14) give the number  18. The 18th Fibonacci number is 2,584.
# Adapted from https://github.com/ianmcloughlin/python-fib/blob/master/fib.py
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 18
ans = fib(x)
print("Fibonacci number", x, "is", ans)
