"""List Utility Functions."""

author = "730475919"


def all(numbers: list[int], target: int) -> bool:
    """Function checking for whether all ints in list are same as given int."""
    if len(numbers) == 0:
        return False  # If list is empty, returning False
    
    idx = 0
    while idx < len(numbers):
        if numbers[idx] != target:
            return False  # If any index value within the list does not equal target, returning False
        idx += 1
    return True  # Returning True if both of above comments did not apply


def max(numbers: list[int]) -> int:
    """Function that returns largest number in list."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")  # If list is empty, raising ValueError

    largest = numbers[0]  # Establishing the first number as the largest to begin with
    idx2 = 1
    while idx2 < len(numbers):
        if numbers[idx2] > largest:
            largest = numbers[idx2]  # Replacing previous largest number with new largest number as you move through the list
        idx2 += 1  # Moving through the list

    return largest  # Returning the largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function that checks if two lists are identical."""
    if len(list1) != len(list2):
        return False  # Returning False if the lengths of the two lists are not identical

    idx3 = 0
    while idx3 < len(list1):  # While index number is less than the length of both lists, since if we've made it this far we now know length of list 1 = length of list 2
        if list1[idx3] != list2[idx3]:
            return False  # Returning false if the lists are not equivalent to each other at any same index number
        idx3 += 1  # Moving through the list

    return True  # Returning true if both of the above conditions did not apply


def extend(list1: list[int], list2: list[int]) -> None:
    """Function that concatenates two lists."""
    for numbers in list2:  # Selecting numbers in list2
        list1.append(numbers)  # Adding those numbers to the end of list1 with the append function