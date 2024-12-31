# Definition of Point class
class Point:
    """Point class used to create points.
    
    Initialize Point object with x and y parameters.

        - param x: represents point coordinate in x axis.
        - param y: represents point coordinate in y axis.
    """
    
    definition: str = """Entidad geometrica abstracta 
    que representa una ubicación en un espacio."""

    def __init__(self, x: float=0, y: float=0):     
        self._x = x
        self._y = y

    def point_setter(self, new_x: float, new_y: float):
        """Positions the point instance in a new x and y coordenate.
        
        - param x: postition in x axis of point instance.
        - param y: postition in y axis of point instance.
        """
        self._x = new_x
        self._y = new_y

    def point_getter(self):
        """Returns x and y Point atributes."""
        return self._x, self._y

    def reset(self):
        """Moves point instance to (0,0) coordenate."""
        self._x = 0
        self._y = 0

    def compute_distance(self, point: "Point") -> float:
        """Calculates distance between two points (point instances) and
        returns the calculated distance which is a float value.
        
        - param point: second point that is compared to the point instance that
        calls this method.
        """

        distance = ((self._x - point._x)**2+(self._y - point._y)**2)**(0.5)
        return distance

    def __str__ (self):
        """Method that returns a string representation of the instance."""
        return f"({self._x},{self._y})"