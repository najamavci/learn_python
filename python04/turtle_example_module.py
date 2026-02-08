import turtle as t

class TurtleDrawer:
    def __init__(self, speed=5):
        t.speed(speed)  # set turtle speed
        self.t = t

    # Function to draw a square
    def draw_square(self, side_length):
        for _ in range(4):
            self.t.forward(side_length)
            self.t.left(90)

    # Move pen without drawing
    def move_next(self, distance=120):
        self.t.penup()
        self.t.forward(distance)
        self.t.pendown()

    # Draw polygon/circle approximation
    def draw_circle(self, steps, step_length, turn_angle):
        for _ in range(steps):
            self.t.forward(step_length)
            self.t.right(turn_angle)

    # Example: draw letter P
    def draw_P(self):
        self.t.left(90)
        self.t.forward(50)
        self.t.right(90)
        self.t.forward(20)
        self.t.right(90)
        self.t.forward(25)
        self.t.right(90)
        self.t.forward(20)
        self.t.penup()
        self.t.right(180)
        self.t.forward(50)
        self.t.pendown()
        self.t.left(90)
        self.t.forward(10)
        self.move_next(30)

    # Example: draw letter Y
    def draw_Y(self):
        self.t.left(45)
        self.t.forward(35)
        self.t.right(90)
        self.t.forward(35)
        self.t.backward(35)
        self.t.left(45)
        self.t.forward(50)
        self.move_next(30)

    # Keep window open
    def done(self):
        t.mainloop()