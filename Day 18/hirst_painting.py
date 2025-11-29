from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

color_list = [(245, 239, 228), (236, 240, 247), (248, 238, 244), (235, 246, 241), (196, 158, 124), (64, 95, 125),
              (142, 87, 62), (139, 162, 184), (216, 209, 128), (184, 147, 159), (23, 36, 54), (122, 78, 93),
              (138, 179, 153), (46, 23, 16), (68, 114, 84), (54, 23, 34), (130, 25, 39), (20, 38, 29), (169, 156, 50),
              (188, 98, 85), (220, 174, 188), (125, 34, 25), (173, 99, 116), (226, 176, 168), (46, 59, 96)]

t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))

    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()
