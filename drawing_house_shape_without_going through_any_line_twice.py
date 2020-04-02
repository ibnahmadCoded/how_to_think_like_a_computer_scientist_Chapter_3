import turtle

window = turtle.Screen()

tess = turtle.Turtle()
tess.pensize(5)

movement = [(0,100), (90,100), (90,100), (90,100), (135, 141.42), (75, 100),
            (120, 100), (75, 141.42)]

for direction, distance in movement:
    tess.left(direction)
    tess.forward(distance)

