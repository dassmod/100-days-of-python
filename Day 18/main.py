import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

t = Turtle()


# def dashed_line(turtle_obj, length, dash_length=10, gap_length=5):
#     distance_covered = 0
#     while distance_covered < length:
#         # Draw a dash
#         turtle_obj.forward(dash_length)
#         distance_covered += dash_length
#
#         # Lift pen and move forward (create gap)
#         turtle_obj.penup()
#         turtle_obj.forward(gap_length)
#         turtle_obj.pendown()
#         distance_covered += gap_length
# dashed_line(t, 200)

# i = 3
# while i <= 10:
#
#     angle = 360 / i
#
#     j = 0
#     while j < i:
#         t.right(angle)
#         t.forward(100)
#         j += 1
#
#     i += 1

angles = [90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

pensize = 10
while 1 > 0:
    t.right(random.choice(angles))
    t.forward(25)
    pensize += 5
    t.pensize(pensize)
    t.pencolor(random_color())



screen.exitonclick()

