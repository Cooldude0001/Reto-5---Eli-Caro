# Imports
from math import degrees, acos, isclose

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


# Definition of Shape class
class Shape:
    """Shape class used to create regular and irregular polygons.
    
    Initialize Shape object with is_regular and vertices parameters.
            
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances). 
        
        Has the following attributes, not necessary to initialize the class:
        - edges: defined using calculate_edges method.
        - inner_angles: defined using calculate_inner_angles method.
    """

    def __init__(self, is_regular: "bool", vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges ()
        self.inner_angles = self.compute_inner_angles ()

    def calculate_edges(self) -> "list[Line]":
        """Calculates instance edges and checks if are regular as specified, 
        returns a list of line instaces."""

        # This list contains the line lengths
        shape_edges = [] 
        
        for index in range(len(self.vertices)):
            start_point = self.vertices [index]
            # To avoid Indexerror exception and make last line between last and
            # start point
            end_point = self.vertices [(index + 1) % len(self.vertices)]
            shape_edges.append(Line(start_point, end_point))
        
        if self.is_regular:
            comparison_length = shape_edges [0].length
            for edge_length in shape_edges:
                if not (isclose(comparison_length, edge_length.length)):
                    raise ValueError("Instance must be regular as specified.")
        
        return shape_edges
    
    def compute_area(self) -> "float":
        """Calculates instance area, returns float value."""
        pass

    def compute_perimeter(self) -> "float":
        """Calculates instance perimeter, returns float value."""
        
        shape_perimeter = 0

        for edges in self.edges:
            shape_perimeter += edges.length
        return shape_perimeter
    
    def compute_inner_angles(self) -> "list":
        pass

    def __str__(self):
        vertices = []
        for point in self.vertices:
            vertices.append(point.__str__())
        return (f"Shape defined using the following vertices {vertices}.")


# Creación de la clase Rectangle (hereda de Shape)
class Rectangle(Shape):
    """Rectangle class used to create rectangles, inherits methods 
    and attributes from Shape class.
    
    Initialize Rectangle object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """

    def __init__(self, is_regular, vertices):
        if len (vertices) != 4: 
            raise ValueError("Rectangle object must have exactly 4 vertices.")
        super().__init__(is_regular, vertices)

    def compute_area(self):
        width = self.edges[0].length
        length = self.edges[1].length
        return width * length

    def compute_inner_angles(self):
        """Calculates instance inner angles, returns a list with inner angles.
        """
        return [90, 90, 90, 90]


# Creacion de la clase Square (hereda de Rectangle)
class Square(Rectangle):
    """Square class used to create squares, inherits methods 
    and attributes from Rectangle class.
    
    Initialize Square object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """
    
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        
        # all edges must have equal length
        a, b, c, d = (edge.length for edge in self.edges)

        if self.is_regular == True:
            if not (a == b and b == c and c == d and d == a):
                raise ValueError (
                    "Square instance must have the same length in all edges.")
        else:
            raise ValueError("Square instance must be regular.")
        

# Creación de la clase Triangle (hereda de Shape)
class Triangle(Shape):
    """Triangle class used to create triangles, inherits methods
    and attributes from Shape class.
    
    Initialize Triangle object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """
        
    def __init__(self, is_regular, vertices):
        if len(vertices) != 3:
            raise ValueError("Triangle instance must have 3 vertices.")
        super().__init__(is_regular, vertices)
    
    def compute_area(self):
        # Heron's formula to calculate any triangle area
        a, b, c = (edge.length for edge in self.edges) # positional asignation
        semiperimter = (a+b+c)/2
        return (semiperimter*(semiperimter-a)*(semiperimter-b)*
               (semiperimter-c))**0.5
    
    def compute_inner_angles(self):
        """Calculates inner angles, returns a list of instance inner angles."""
        
        angles = []
        a,b,c = (edge.length for edge in self.edges)
        
        a_angle = degrees(acos(((b**2 + c**2) - a**2)/(2*b*c)))
        b_angle = degrees(acos(((a**2 + c**2) - b**2)/(2*a*c)))
        c_angle = degrees(acos(((a**2 + b**2)- c**2)/(2*b*a)))
        
        angles.append (a_angle) 
        angles.append (b_angle) 
        angles.append (c_angle)
        return angles
    

# Creación de la clase Equilateral (hereda de Triangle)
class Equilateral(Triangle):
    """Equilateral class used to create equilateral triangles, inherits methods
    and attributes from Triangle class.
    
    Initialize Equilateral object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == False:
            raise ValueError("Equilateral instance must be regular.")
        
        # Equilateral triangles must have the same length in all edges
        a, b, c = (edge.length for edge in self.edges)
        
        if not (a == b and b == c):
            raise ValueError (
                "Equilateral instance must have the same length in all edges.")


# Creación de la clase Isosceles (hereda de Triangle)
class Isosceles(Triangle):
    """Isosceles class used to create isosceles triangles, inherits methods
    and attributes from Triangle class.
    
    Initialize Isosceles object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Isosceles instance can't be regular.")
        
        # Check if vertices form an Isosceles triangle
        a, b, c = (edge.length for edge in self.edges)
        
        # isosceles condition is a boolean variable that determines if
        # the instance is an isosceles triangle if only 2 lengths are equal
        isosceles_condition = (
            isclose(a, b) and not isclose(b, c) or
            isclose(b, c) and not isclose(c, a) or
            isclose(a, c) and not isclose(a, b)
        )

        if not isosceles_condition:
            raise ValueError(
        "Isosceles instance can't be constructed using the given vertices.")

# Creación de la clase Scalene (hereda de Triangle)
class Scalene(Triangle):
    """Scalene class used to create scalene triangles, inherits methods
    and attributes from Triangle class.
    
    Initialize Scalene object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Scalene instance can't be regular.")
        
        # Scalene triangles has different edge lengths
        a, b, c = (edge.length for edge in self.edges)

        # scalene_condition verifies if all edge lengths are different
        scalene_condition = (
            not isclose (a,b) and 
            not isclose (b,c) and 
            not isclose (a,c)
        )

        if not scalene_condition:
            raise ValueError(
        "Scalene instance can't be constructed using the given vertices.")


# Creación de la clase Trirectangle (hereda de Triangle)
class Trirectangle(Triangle):
    """Trirectangle class used to create right triangles, inherits methods
    and attributes from Triangle class.
    
    Initialize Trirectangle object with is_regular and vertices parameters.
        
        - param is_regular: has a boolean value that represents if the
        instance is regular or not.
        - param vertices: list of point instances used to create instance
        edges (line instances).
    """

    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        # check if the shape is regular
        if self.is_regular == True:
            raise ValueError("Trirectangle class cannot be regular")
        
        # Returns true if length of c**2 is equal to a**2 + b**2
        # uses Pytagora's theorem
        
        a, b, c = sorted(edge.length for edge in self.edges)
        # In this case it will evalue if the sum of squares is "more of less"
        # equal to c**2
        if not (c**2 - (10**-9)) < (a**2 + b**2) <= c**2:
            raise ValueError(
            "Trirectangle instance cannot be formed with the given vertices.")