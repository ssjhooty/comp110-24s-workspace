"""CQ08."""
from __future__ import annotations

__author__ = "730475919"


class Point:
    """Class named 'Point'."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Init function."""
        self.x = x_init
        self.y = y_init

    def scale_by(self: int, factor: int) -> None:
        """Method that updates x and y attruibutes."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self: int, factor: int) -> Point:
        """Method that returns x and y attributes in a new point."""
        return Point(self.x * factor, self.y * factor)
    