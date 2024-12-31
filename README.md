# 📦 Reto-5---Eli-Caro
Teniendo en cuenta la clase de POO orientada a la creación de paquetes y módulos, este reto consiste en la separación por módulos y paquetes del ejercicio de geometría del reto anterior
en dos enfoques diferentes: la creación de un paquete que contenga todas las clases del ejercicio en un solo módulo y la creación de un paquete que contenga varios módulos.

## Estuctura de paquetes y modulos
La estructura final para el reto es la siguiente:

```bash
└── Shapes/  # Paquete con modulos individuales
    ├── __init__.py
    ├── Line_class.py  # Contiene la clase Line
    ├── Point_class.py  # Contiene la clase Point
    ├── Quadrilaterals.py  # Contiene las clases Rectangle y Square
    ├── Shape_class.py  # Contiene la clase Shape
    └── Triangles.py  # Contiene las clases Triangle, Equilateral, Isosceles, Scalene y Trirectangle
└── Shapes_deluxe_ver/  #Paquete con un solo modulo individual
    ├── __init__.py  
    └── Geometry.py 
├── main.py  # Archivo principal que contiene código de prueba para cada clase  
```

 ## Ejecución del archivo main
El archivo `main.py` al ser ejecutado como archivo principal, permite probar ambas situaciones de importación de paquetes, a través de un "menú" de opciones.
Al ejecutar el archivo `main.py` el output esperado para ambas situaciones es:

```bash
    - Point, line and shape test:

    point definition: (3,2)      
    distance between points: 4.47213595499958
    line definition: Line instance defined between (3,2) and (1,2) points.
    line slope: 0.0
    shape definition: Shape defined using the following vertices
    ['(2,1)', '(5,1)', '(5.93,3.85)', '(3.5,5.62)', '(1.07,3.85)'].
    shape's perimeter: 15.008385326680383

    - Quadrilatereals test:

    rectangle's perimeter: 12.0
    rectangle's area: 8.0²
    square's perimeter: 12.0
    square's area: 9.0²

    - Triangles test:

    normal_triangle perimeter: 7.63441361516796
    normal_triangle area: 2.5000000000000013²

    equilateral_triangle perimeter: 6.0
    equilateral_triangle area: 1.7320508075688772²

    isosceles_triangle perimeter: 8.0
    isosceles_triangle area: 3.0²

    scalene_triangle perimeter: 11.404918347287666
    scalene_triangle area: 3.0²

    right_angled_triangle perimeter:12.0
    right_angled_triangle area: 6.0²
```
