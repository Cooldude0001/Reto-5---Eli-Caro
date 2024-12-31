# Importaciones
from math import isclose
from Line_class import  Line
from Point_class import Point

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