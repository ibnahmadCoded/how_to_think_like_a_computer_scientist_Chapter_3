import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.speed(10)

turns = [(160,20), (-43,10), (270,8), (-43,12)]

for direction, distance in turns:
    tess.left(direction)
    tess.forward(distance)

print("Pirate is currently at coordinate:", tess.position())
print("Pirate's current heading is:",tess.heading())
