def sum(n):
    """
    :type n: int
    :rtype: int
    """
    # Fill out,  Use recursion
    if n > 1:
        return n + sum(n - 1)
    else:
        return 1


def fibonacci(n):
    """:
    :type n: int
    :rtype: int
    """
    # Fill out,  Use recursion
    if n > 1:
        return fibonacci(n - 2) + fibonacci(n - 1)
    elif n == 0:
        return 0
    else:
        return 1


def factorial(n):
    """
    :type n: int
    :rtype: int
    """
    # Fill out,  Use recursion
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def decimal_to_binary(n):
    """:
    :type n: int
    :rtype: int
    """
    # Fill out,  Use recursion
    if n > 1:
        return n % 2 + decimal_to_binary(n / 2) * 10
    elif n == 0:
        return 0
    else:
        return 1


def TestRecursionFunction():
    print factorial(10)
    print sum(100)
    print fibonacci(10)
    print decimal_to_binary(15)


TestRecursionFunction()
