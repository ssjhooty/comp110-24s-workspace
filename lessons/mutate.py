"""Mutating functions."""
__author__ = "730475919"


def manual_append(lst: list[int], num: int) -> None:
    lst.append(num)


def double(lst: list[int]) -> None:
    index = 0
    while index < len(lst):
        lst[index] *= 2
        index += 1