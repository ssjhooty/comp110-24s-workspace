"""Testing Dictionary Utility Functions."""

__author__ = "730475919"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_normal_1() -> None:
    """We must test inverting when the input dictionary is not empty."""
    non_inverted = {"a": "apple", "b": "banana", "c": "cherry"}
    expected_output = {"apple": "a", "banana": "b", "cherry": "c"}
    result = invert(non_inverted)
    assert result == expected_output


def test_invert_edge() -> None:
    """We must test inverting when inverting would lead to duplicate values."""
    with pytest.raises(KeyError):
        non_inverted = {"a": "apple", "b": "banana", "c": "apple"}
        invert(non_inverted)


def test_invert_normal_2() -> None:
    """We must test inverting when the input dictionary is empty."""
    non_inverted = {}
    expected_output = {}
    result = invert(non_inverted)
    assert result == expected_output


def test_favorite_color_normal_1() -> None:
    """We must test picking the most popular color when the input color dictionary is not empty."""
    color_dict = {"John": "blue", "Alice": "green", "Bob": "blue", "Eve": "red"}
    expected_output = "blue"
    result = favorite_color(color_dict)
    assert result == expected_output


def test_favorite_color_edge() -> None:
    """We must test picking the most popular color when there are multiple favorites."""
    color_dict = {"John": "blue", "Alice": "green", "Bob": "blue", "Eve": "green"}
    expected_output = "blue", "green"
    result = favorite_color(color_dict)
    assert result == expected_output


def test_favorite_color_normal_2() -> None:
    """We must test picking the most popular color when the input color dictionary is empty."""
    color_dict = {}
    expected_output = {}
    result = favorite_color(color_dict)
    assert result == expected_output


def test_count_normal_1() -> None:
    """We must test counting the prevalence of each item when the input list is not empty."""
    values_to_count = ["a", "b", "c", "a", "b", "c", "a"]
    expected_output = {"a": 3, "b": 2, "c": 2}
    result = count(values_to_count)
    assert result == expected_output


def test_count_edge() -> None:
    """We must test counting the prevalence of each item when there is only one item."""
    values_to_count = ["a", "a", "a"]
    expected_output = {"a": 3}
    result = count(values_to_count)
    assert result == expected_output


def test_count_normal_2() -> None:
    """We must test counting the prevalence of each item when the input list is empty."""
    values_to_count = []
    expected_output = {}
    result = count(values_to_count)
    assert result == expected_output

 
def test_alphabetizer_normal_1() -> None:
    """We must test alphabetizing items when the input word list is not empty."""
    word_list = ["apple", "banana", "cherry", "apricot"]
    expected_output = {"a": ["apple", "apricot"], "b": ["banana"], "c": ["cherry"]}
    result = alphabetizer(word_list)
    assert result == expected_output


def test_alphabetizer_edge() -> None:
    """We must test alphabetizing items when there is only one first letter."""
    word_list = ["apple", "apricot"]
    expected_output = {"a": ["apple", "apricot"]}
    result = alphabetizer(word_list)
    assert result == expected_output


def test_alphabetizer_normal_2() -> None:
    """We must test alphabetizing items when the input word list is empty."""
    word_list = []
    expected_output = {}
    result = alphabetizer(word_list)
    assert result == expected_output


def test_update_attendance_normal_1() -> None:
    """We must test updating attendace when the input word list is not empty."""
    attendance_dict = {'Monday': ['John', 'Alice'], 'Tuesday': ['Bob']}
    day = 'Monday'
    student = 'Eve'
    expected_output = {'Monday': ['John', 'Alice', 'Eve'], 'Tuesday': ['Bob']}
    result = update_attendance(attendance_dict, day, student)
    assert result == expected_output


def test_update_attendance_edge() -> None:
    """We must test updating attendace when we are adding a new day."""
    attendance_dict = {'Monday': ['John', 'Alice'], 'Tuesday': ['Bob']}
    day = 'Wednesday'
    student = 'Eve'
    expected_output = {'Monday': ['John', 'Alice'], 'Tuesday': ['Bob'], 'Wednesday': ['Eve']}
    result = update_attendance(attendance_dict, day, student)
    assert result == expected_output


def test_update_attendance_normal_2() -> None:
    """We must test updating attendace when the input word list is empty."""
    attendance_dict = {}
    day = 'Monday'
    student = 'Eve'
    expected_output = {'Monday': ['Eve']}
    result = update_attendance(attendance_dict, day, student)
    assert result == expected_output