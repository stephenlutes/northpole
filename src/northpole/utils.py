from __future__ import annotations


class CartesianPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def down(self) -> CartesianPoint:
        """
        Return the next coordinate down from the point.

        Returns:
            CartesianPoint: The point that is one unit down from the current point.
        """
        return CartesianPoint(self.x, self.y - 1)

    def left(self) -> CartesianPoint:
        """
        Return the next coordinate left from the point.

        Returns:
            CartesianPoint: The point that is one unit to the left from the current
            point.
        """
        return CartesianPoint(self.x - 1, self.y)

    def right(self) -> CartesianPoint:
        """
        Return the next coordinate right from the point.

        Returns:
            CartesianPoint: The point that is one unit to the right from the current
            point.
        """
        return CartesianPoint(self.x + 1, self.y)

    def up(self) -> CartesianPoint:
        """
        Return the next coordinate up from the point.

        Returns:
            CartesianPoint: The point that is one unit up from the current point.
        """
        return CartesianPoint(self.x, self.y + 1)

    def __eq__(self, obj) -> bool:
        return self.x == obj.x and self.y == obj.y

    def __ne__(self, obj) -> bool:
        return not self.__eq__(obj)

    def __hash__(self):
        return hash((self.x, self.y))
