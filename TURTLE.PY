import turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen =turtle.Turtle()
pen.pensize(3)
pen.speed(2)

pen.color("red")
for _ in range(4):
    pen.forward(100)
    pen.right(90)
pen.penup()
pen.goto(-150, 0)
pen.pendown()

pen.color("green")
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.penup()
pen.goto(150, 0)
pen.pendown()

pen.color("blue")
pen.circle(50)

turtle.done
