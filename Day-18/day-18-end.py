#####Turtle Intro######

from turtle import Turtle
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.forward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(90)
timmy_the_turtle.setheading(180)


########Square############
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


########Modules###########

import turtle
jimmy = turtle.Turtle()

from turtle import Turtle
timmy = Turtle()

from turtle import *

import turtle as t
tommy = t.Turtle()


###########Dashed Line########
for _ in range(50):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


########Shapes###########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

import turtle as t
import random
tim = t.Turtle()


def draw_shape(num_sides, distance):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.right(angle)
        tim.forward(distance)


for side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(side_n, 100)



#########Random Walk#############
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    random_r = random.randint(0, 255)
    random_g = random.randint(0, 255)
    random_b = random.randint(0, 255)
    random_color = (random_r, random_g, random_b)
    return  random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)



############Spirograph###############
tim = t.Turtle()
def spirograph(size):
    tim.speed("fastest")
    for _ in range(0, int(360 / size)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size)
        tim.circle(100)

spirograph(5)

