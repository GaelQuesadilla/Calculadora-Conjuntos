
"""
Las funciones que utiliza el evaluador de funciones para generar el conjunto
"""


def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def even(n):
    return 2*n


def odd(n):
    return 2*n - 1


def div(x, y):
    return x/y


def mult(x, y):
    return x * y


def pow(x, y):
    return x**y
