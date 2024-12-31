# Importaciones
from Point_class import Point

# Definition of Line class
class Line:
    """Line class used to create lines.

    Initialize Line object with start_point and end_point parameters.

        - param start_point: represents start point of line.
        - param end_point: represents end point of line.
            
        Has length attribute that represents line length, not necessary to
        initialize this class.
    """

    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start = start_point
        self.end = end_point
        self.length = self.compute_length()

    def compute_length(self):
        """Calculates the distance between start and end points, returns the 
        calculated distance which is a float value.
        """
        return self.start.compute_distance(self.end) 

    def compute_slope(self):
        """Calculates line slope, returns float value."""

        # Vertical difference / horizontal difference
        return (self.start._y - self.end._y) / (self.start._x - self.end._x)

    def compute_horizontal_cross(self):
        """Determines if line instance cross x axis, returns False if doesn't 
        or intersection point and True if it exist."""
        
        if self.start._y * self.end._y > 0:
            return False
        if self.start._y == self.end._y:
            return False
        x_cross = self.start._x - (self.start._y * (
                  self.end._x - self.start._x)) / (self.end._y - self.start._y)
        return Point(x_cross, 0), True

    def compute_vertical_cross(self):
        """Determines if line instance cross y axis, returns False if doesn't 
        or intersection point and True if it exist.
        """
        
        if self.start._x * self.end._x > 0:
            return False
        if self.start._x == self.end._x:
            return False
        y_cross = self.start._y - (self.start._x * (
                  self.end._y - self.start._y)) / (self.end._x - self.start._x)
        
        return Point(0, y_cross), True
    
    def __str__(self):
        """Method that returns a string representation of the instance."""
        return (
        f"Line instance defined between {self.start} and {self.end} points.")