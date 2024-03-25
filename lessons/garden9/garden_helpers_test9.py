"""Testing Garden Functions."""
__author__ = "730475919"


from lessons.garden9.garden_helpers9 import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_if_we_add_plant_to_empty_kind_list_whether_it_actually_adds() -> None:
    """We must add plants to an empty kind list."""
    assert add_by_kind({}, "flower", "tulip") == {"flower": "tulip"}


def test_if_we_add_plant_to_populated_kind_list_whether_it_actually_adds() -> None:
    """We must add plants to a populated kind list."""
    assert add_by_kind({"flower": "rose"}, "flower", "tulip") == {"flower": ["rose", "tulip"]}


def test_if_we_add_plant_to_empty_date_list_whether_it_actually_adds() -> None:
    """We must add plants to an empty date list."""
    assert add_by_date({}, "October", "tulip") == {"October": "tulip"}


def test_if_we_add_plant_to_populated_date_list_whether_it_actually_adds() -> None:
    """We must add plants to a populated date list."""
    assert add_by_date({"October": "rose"}, "October", "tulip") == {"October": ["rose", "tulip"]}


def test_lookup_by_kind_and_date_for_a_previously_empty_list() -> None:
    """We must create a kind and date list for an empty list with additions."""
    assert lookup_by_kind_and_date({}, {}, "flower", "October") == {"flower": "October"}


def test_lookup_by_kind_and_date_for_a_previously_populated_list() -> None:
    """We must create a kind and date list for a populated list with additions."""
    assert lookup_by_kind_and_date({"flower": "rose"}, {"October": "rose"}, "flower", "October") == {"flower": "October"}