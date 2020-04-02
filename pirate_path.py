import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.speed(10)

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for turn in turns:
    tess.left(turn)
    tess.forward(100)

print("Pirate is currently at coordinate:", tess.position())
print("Pirate's current heading is:",tess.heading())
