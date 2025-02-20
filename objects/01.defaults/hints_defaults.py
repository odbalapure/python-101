import math

class Point:
    """
    Represent a point in 2D geometric coordinates
    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p1)
    >>> 5.0
    """
    def __init__(
            self, 
            x: float = 0, 
            y: float = 0
    ) -> None:
        """
        Initialize position of a point. The x and y
        coordinates can be specified. If they are not,
        the point is initialized to the origin.
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location in 2D space
        :param x: float x-coordinate
        :param y: float y-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Resets the position to the origin
        """
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate Euclidean distance from the origin
        to a second point passed as a parameter
        :param other: Point instance
        :return: float distance
        """
        return math.hypot(self.x - other.x, self.y - other.y)
    
# python3 -i hints_defaults.py
# help(Point)
# quit()
p_1 = Point()
p_2 = Point(3, 4)
print(p_1.calculate_distance(p_2))
