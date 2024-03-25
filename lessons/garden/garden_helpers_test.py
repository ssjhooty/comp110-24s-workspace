"""Testing Garden Functions."""
__author__ = "730475919"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_if_we_add_plant_to_empty_kind_list_whether_it_actually_adds() -> None:
    """We must add plants to an empty kind list."""
    result = {}
    add_by_kind(result, "flower", "tulip")
    assert result == {"flower": ["tulip"]}  # Assert the expected result


def test_if_we_add_plant_to_populated_kind_list_whether_it_actually_adds() -> None:
    """We must add plants to a populated kind list."""
    result = {"flower": ["rose"]}
    add_by_kind(result, "flower", "tulip")
    assert result == {"flower": ["rose", "tulip"]}  # Assert the expected result


def test_if_we_add_plant_to_empty_date_list_whether_it_actually_adds() -> None:
    """We must add plants to an empty date list."""
    result = {}
    add_by_date(result, "October", "tulip")
    assert result == {"October": ["tulip"]}  # Assert the expected result


def test_if_we_add_plant_to_populated_date_list_whether_it_actually_adds() -> None:
    """We must add plants to a populated date list."""
    result = {"October": ["rose"]}
    add_by_date(result, "October", "tulip")
    assert result == {"October": ["rose", "tulip"]}  # Assert the expected result


def test_lookup_by_kind_and_date_for_a_previously_empty_list() -> None:
    """We must create a kind and date list for an empty list with additions."""
    result = {}
    assert lookup_by_kind_and_date({}, {}, "flower", "October") == "No flowers to plant in October."


def test_lookup_by_kind_and_date_for_a_previously_populated_list() -> None:
    """We must create a kind and date list for a populated list with additions."""
    result = {"flower": ["rose"], "October": ["rose"]}
    assert lookup_by_kind_and_date(result, result, "flower", "October") == "flowers to plant in October: ['rose']"