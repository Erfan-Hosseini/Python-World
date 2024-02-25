import turtle
import random


turtle.bgcolor("black")

polygon = turtle.Turtle()
polygon.speed(5)

def draw_polygon(n, size, color):
    angle = 360 / n
    polygon.color(color)
    for _ in range(n):
        polygon.forward(size)
        polygon.left(angle)

for sides in range(3, 20):

    size = sides * 20
    
    polygon_color = (random.random(), random.random(), random.random())

    polygon.penup()
    polygon.setpos(-size / 2, -size / 2)
    polygon.pendown()
    draw_polygon(sides, size, polygon_color)

