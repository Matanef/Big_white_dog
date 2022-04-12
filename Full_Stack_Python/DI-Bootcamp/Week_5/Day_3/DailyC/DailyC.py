from turtle import circle


class Circle:

    def __init__(self, radius):
       print("created by init") 
       pass

    @classmethod
    def from_diameter(cls, diameter):
        print("Createdby class method")
        pass

circle = Circle(radius = 5)
circle = Circle.from_diameter(diameter = 2)
