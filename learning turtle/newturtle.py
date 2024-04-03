import turtle
turtle.shape('turtle')
for j in range(0,360):
    turtle.forward(1)
    turtle.left(1)
    for i in range(0,6):
        turtle.forward(50)

        turtle.right(72)

turtle.exitonclick()

