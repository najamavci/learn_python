from python04.turtle_example_module import TurtleDrawer

drawer = TurtleDrawer(speed=7)

# Draw squares
drawer.draw_square(50)
drawer.move_next(60)
drawer.draw_square(30)

# Draw a circle
drawer.draw_circle(36, 10, 10)

# Draw letters
drawer.draw_P()
drawer.draw_Y()
# You can add T, H, O, N similarly

# Keep the turtle window open
drawer.done()