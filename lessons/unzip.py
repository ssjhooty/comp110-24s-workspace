"""Splitting a dictionary into two lists."""
__author__ = "730475919"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Producing a list of all the keys in the input dictionary."""
    return list(input_dict.keys())


def get_values(input_dict: dict[str, int]) -> list[int]:
    """Producing a list of all the values in the input dictionary."""
    return list(input_dict.values())