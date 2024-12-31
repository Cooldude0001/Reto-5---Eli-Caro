# Imports
from math import degrees, acos, isclose
from Shape_class import Shape

# Definition of Triangle class
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
    
# Class Equilateral (Inherit methods and attributes from Triangle class)
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


# Class Isosceles (Inherit methods and attributes from Triangle class)
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


# Class Scalene (Inherit methods and attributes from Triangle class)
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


# Class Trirectangle (Inherit methods and attributes from Triangle class)
class Trirectangle(Triangle):
    """Trirectangle class used to create right triangles, inherits methods
    and attributes from Triangle class.
    
    Initialize Rectangle object with is_regular and vertices parameters.
        
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