"""Dictionary Utility Functions."""

__author__ = "730475919"


def invert(non_inverted: dict[str, str]) -> dict[str, str]:
    """Function that inverts a dictionary."""
    inverted = {}
    for key in non_inverted:
        value = non_inverted[key]
        if value in inverted:  # If a to-be key has already been recorded
            raise KeyError()  # Raise a key error
        inverted[value] = key
    return inverted


def favorite_color(color_dict: dict[str, str]) -> str:
    """Function that returns the most popular color."""
    most_popular_color: str = ""
    color_count: int = 0
    color_counter: dict[str, int] = {} 
    for color in color_dict:
        if color_dict[color] in color_counter:
            color_counter[color_dict[color]] += 1  # Adding one each time the color appears again
        else:
            color_counter[color_dict[color]] = 1  # Establishing a frequency of one the first time a color appears
    for color in color_counter:
        if color_counter[color] > color_count:
            most_popular_color = color
            color_count = color_counter[color]
    return most_popular_color


def count(values_to_count: list[str]) -> dict[str, int]:
    """Function that counts the frequencies of a list of values and returns a dictionary of each of the items."""
    frequency_dict: dict[str, int] = {}
    for item in values_to_count:
        if item in frequency_dict:
            frequency_dict[item] += 1  # Adding one to the counter if it has already been established
        else:
            frequency_dict[item] = 1  # Establishing the counter at an initial value of 1
    return frequency_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Function that creates an alphabetized dictionary from a list of words."""
    categorized_words: dict[str, list[str]] = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in categorized_words:
            categorized_words[first_letter].append(word)  # Creating a pre-existing dicionary entry at a given letter
        else:
            categorized_words[first_letter] = [word]  # Creating a new dictionary entry at a given letter
    return categorized_words


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Function that updates a dictionary based attendance log."""
    if day in attendance_dict:
        attendance_dict[day].append(student)  # Continueing the attendance log for a given day
    else:
        attendance_dict[day] = [student]  # Starting the attendance log for a given day