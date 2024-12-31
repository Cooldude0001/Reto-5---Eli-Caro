# Imports
import Shape_class as Shape

# Class Rectangle (Inherit methods and attributes from Shape class)
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


# Class Square (Inherit methods and attributes from Rectangle class)
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