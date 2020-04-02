import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.speed(1)

#drawing equalateral triangle
for _ in range(3):
    tess.forward(100)
    tess.left(120)

#drawing rectangle
for _ in range(4):
    tess.forward(100)
    tess.left(90)

#drawing hexagon
for _ in range(6):
    tess.forward(100)
    tess.left(60)

#drawing octagon
for _ in range(8):
    tess.forward(100)
    tess.left(45)
