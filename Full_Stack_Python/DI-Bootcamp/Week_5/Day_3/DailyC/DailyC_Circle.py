class Circle:

    def __init__(self, radius = None, diameter = None):
        if radius == None and diameter == None:
            self.__radius = 1
            self.__diameter = self.__radius * 2
            print("Radius: 1, diameter: 2")
            
        elif radius != None and diameter == None:
            self.__radius = radius
            self.__diameter = radius * 2
            print(f"Radius: {self.__radius}, diameter: {self.__diameter}")
        elif radius == None and diameter != None:
            self.__diameter = diameter
            self.__radius = self.__diameter // 2
            print(f"Radius: {self.__radius}, diameter: {self.__diameter}")
        else:
            user_input = input("Please provide valid input.").split()
            return Circle(user_input)
    @property
    def compute_area(self):
        return self.__radius * self.__diameter
    def __add__(self, circle):
        return self.compute_area + circle.compute_area
    def __lt__(self, circle):
        if self.compute_area < circle.compute_area:
            return True
        else:
            return False
    def __eq__(self, circle):
        if self.compute_area == circle.compute_area:
            return True
        else:
            return False
    def __le__(self, circle):
        if self.compute_area <= circle.compute_area:
            return True
        else:
            return False

circle_a = Circle(diameter = 8)
circle_b = Circle(diameter = 6)
circle_a + circle_b
circle_a < circle_b
circle_a == circle_b
circle_list = [circle_a, circle_b]
sorted(circle_list)
print(circle.diameter)
circle.radius
circle_a.compute_area