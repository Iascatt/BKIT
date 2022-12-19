"""
A000108		Catalan numbers
Recurrence: a(n) = Sum_{k=0..n-1} a(k)a(n-1-k)
"""


def catalan(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    return sum(map(lambda i: catalan(i) * catalan(n - 1 - i), range(n)))

