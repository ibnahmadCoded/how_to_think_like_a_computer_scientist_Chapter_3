import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

tess.stamp()

for _ in range(12):
    tess.penup()
    tess.forward(120)
    tess.pendown()
    tess.forward(30)
    tess.penup()
    tess.forward(30)
    tess.stamp()
    tess.backward(180)
    tess.left(30)

window.mainloop()
