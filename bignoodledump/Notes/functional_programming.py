"""
kwargs is a dictionary
dict().get returns a value if it cant return keyed index
itertools is great for functional programming

PURE FUNCTIONS: Depend only on their arguments, very good because of memoization
IMPURE FUNCTIONS: Depend on other things, kinda scuff
"""


def mydecorator(func):
    def wrapper():
        print("Initalizing...")
        func()
        print("Exiting...")
    return wrapper


@mydecorator
def vectorscalar(v, s):  # map example
    return list(map(lambda x: x*s, v))


@mydecorator
def five_goes_into(n):  # filter example
    return list(filter(lambda x: x % 5 > 0, n))


# How to decorate a generator??
def generator():  # generator example
    for i in range(10):  # makes an iterable from 1 to 9
        yield i


# How to decorate recusive function?
def factorial(n):
    if n == 1:  # Base case, a case that isn't recusive
        return 1
    else:  # recursive cases
        return n * factorial(n - 1)


# how to decorate this pair of functions? how to add a lambda?
def is_even(x):
    """
    I had a cool idea but I have a headache and fucking forgot
    Maybe make my own function like this
    """
    if x == 0:
        return True
    else:
        return is_odd(x-1)


def is_odd(x):
    return not is_even(x)


if __name__ == '__main__':
    print(list(generator()))
    print(factorial(10))
