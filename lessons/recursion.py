"""Turning a standard function into a recursive one."""


def f(n: int, k: int) -> int:
    """Defining the recursive function."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return k + f(n - 1, k)