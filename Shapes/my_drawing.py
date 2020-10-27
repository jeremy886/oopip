from Shapes.my_shapes import Paper, Triangle, Rectangle, Oval


paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_x(50)
rect1.set_y(150)
rect1.set_color("blue")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(300)
rect2.set_height(100)
rect2.set_cx(0)
rect2.set_cy(0)
rect2.set_color("pink")
rect2.draw()



# Oval with setters
oval2 = Oval()
oval2.set_height(200)
oval2.set_width(100)
oval2.set_color("fuchsia")
oval2.set_x(30)
oval2.set_y(90)
oval2.draw()


o1 = Oval()
o1.randomize()
o1.draw()

tri = Triangle(0, 0, 100, 5, 100, 200)
tri.draw()

paper.display()