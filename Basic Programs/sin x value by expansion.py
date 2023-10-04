import math


angle = 90


def factorial(n):
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial = n_factorial * i
    return n_factorial


def nth_term_sine_expansion(x, n):
    term = ((-1) ** (n - 1)) * (x ** (2 * n - 1)) / factorial(2 * n - 1)
    return term


def sin_value(degrees, n):
    radian = math.radians(degrees)
    final_value = 0
    for i in range(1, n + 1):  # Changed the range to include the nth term
        value = nth_term_sine_expansion(radian, i)
        final_value = final_value + value
    return final_value


print(sin_value(angle, 11))
print(math.sin(math.radians(angle)))
