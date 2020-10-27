from Shapes.shapes import Paper, Triangle, Oval


paper = Paper()

o1 = Oval()
o1.randomize()
o1.draw()

# Oval with setters
oval2 = Oval()
oval2.set_height(200)
oval2.set_width(100)
oval2.set_color("fuchsia")
oval2.set_x(30)
oval2.set_y(90)
oval2.draw()

tri = Triangle(15, 50, 100, 5, 100, 200)
tri.draw()

paper.display()