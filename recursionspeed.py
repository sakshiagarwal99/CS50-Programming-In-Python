setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""

from timeit import timeit

tm = timeit("factorial(4)", setup=setup_string, number=10000000)
print(tm)