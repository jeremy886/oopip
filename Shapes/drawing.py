from shapes import Paper, Rectangle

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
# rect1.set_x(100)
# rect1.set_y(200)
rect1.draw()

rect2 = Rectangle()
rect2.set_width(300)
rect2.set_height(100)
rect2.set_x(0)
rect2.set_y(0)
rect2.set_color("pink")
rect2.draw()

paper.display()