# import colorgram

# colors = colorgram.extract('image.jpg',30)

# rgb_colors = []


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

from turtle import Turtle, Screen
import random

color_list = [(232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

#10 by 10
# 20  _50_ 20

turtle = Turtle()
turtle.shape("turtle")
turtle.speed("fastest")
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.goto((-screen.window_width() //2) + 100 , (-screen.window_height() //2) + 100)
turtle.pendown()


def draw_circle(radius):
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

def step_forward():
    turtle.forward(70)

def step_up():
    turtle.left(90)
    step_forward()
    turtle.right(90)

def get_to_start_of_line():
    step_up()
    turtle.left(180)
    for i in range(10):
        step_forward()
    turtle.left(180)

def change_color(color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    
def draw_circle_filled(radius):
    turtle.begin_fill()
    draw_circle(radius)
    turtle.end_fill()

def draw_line(color_list):
    for i in range(10):
        color = random.choice(color_list)

        change_color(color)
        draw_circle_filled(20)
        step_forward()
    get_to_start_of_line()

def draw_picture(color_list):
    for i in range(10):
        draw_line(color_list)



draw_picture(color_list)

screen.exitonclick()