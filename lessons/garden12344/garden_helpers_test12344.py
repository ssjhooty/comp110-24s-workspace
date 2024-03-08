"""Test my garden functions."""

__author__ = "730475919"

import unittest
from lessons.garden12344.garden_helpers12344 import Garden_Functions

class TestGardenFunctions(unittest.TestCase):

    def test_add_by_kind_empty_garden(self):
        """Test if we can add a new plant to an empty garden dictionary."""
        garden_dict = {}
        add_by_kind(garden_dict, "flower", "orchid")
        self.assertEqual(garden_dict, {"flower": ["orchid"]})

    def test_add_by_kind_existing_kind(self):
        """Check to see if we can add a new plant to our existing garden."""
        garden_dict = {"flower": ["tulip", "hibiscus"], "vegetable": ["onion"]}
        add_by_kind(garden_dict, "flower", "rose")
        self.assertEqual(garden_dict, {"flower": ["hibiscus", "rose", "tulip"], "vegetable": ["onion"]})

    def test_add_by_date_new_month(self):
        """Test the addition of a plant to a month that has not already been listed in our garden."""
        garden_dict = {"November": ["lily"], "December": ["onion"]}
        add_by_date(garden_dict, "October", "plumeria")
        self.assertEqual(garden_dict, {"November": ["lily"], "December": ["onion"], "October": ["plumeria"]})

    def test_add_by_date_existing_month(self):
        """Test if we can add a new plant to a month that already has been listed in our garden."""
        garden_dict = {"November": ["lily"], "December": ["onion"]}
        add_by_date(garden_dict, "November", "daffodil")
        self.assertEqual(garden_dict, {"November": ["daffodil", "lily"], "December": ["onion"]})

    def test_lookup_by_kind_and_date_no_plant(self):
        """Test if there are any fruits to plant in a certain month where we expect none (December)."""
        by_kind = {"flower": ["tulip", "hibiscus"], "vegetable": ["onion"]}
        by_date = {"November": ["lily"], "December": ["onion"]}
        result = lookup_by_kind_and_date(by_kind, by_date, "fruit", "December")
        self.assertEqual(result, "No fruits to plant in December.")

    def test_lookup_by_kind_and_date_some_plants(self):
        """Verify the list of flowers to plant in a month in which there is the expectation that flowers will be planted."""
        by_kind = {"flower": ["tulip", "hibiscus"], "vegetable": ["onion"]}
        by_date = {"November": ["lily"], "December": ["onion"]}
        result = lookup_by_kind_and_date(by_kind, by_date, "flower", "November")
        self.assertEqual(result, "flowers to plant in November: ['lily']")

if __name__ == '__main__':
    unittest.main()