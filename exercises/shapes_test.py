from shapes import Circle, Rectangle

def draw_shapes():
    shapes = []
    i = int(input("give me a number: "))
    sally = Circle(i)
    shapes.append(sally)
    for shape in shapes:
        shape.draw()
        print()

draw_shapes()