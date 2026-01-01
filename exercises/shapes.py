class Shape:
    def draw(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        for _ in range(self.height):
            print("*" * self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        r = self.radius
        for y in range(-r, r + 1):
            for x in range(-2*r, 2*r + 1):
                if (x/2)*(x/2) + y*y <= r*r:
                    print("I", end="")
                else:
                    print(" ", end="")
            print()

