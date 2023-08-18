ZERO = 1e-8


def is_zero(x):
    return abs(x) < ZERO


def is_equal(a, b):
    return abs(a - b) < ZERO