from turtle import *

for i in range(3):
    color('blue')
    forward(256)
    left(120)

    for i in range(3):
        color('red')
        forward(128)
        left(120)

        for i in range(3):
            color('green')
            forward(64)
            left(120)

            for i in range(3):
                color('orange')
                forward(32)
                left(120)


exitonclick()

# forward(longueur)
# backward(longueur)
# right(angle)
# left(angle)
# setheading(direction)
# goto(x,y)
# setx(newx)
# sety(newy)
# down()
# up()
# width(epaisseur)
# color(couleur)
# position()
# heading()
# towards(x,y)
# exitonclick()
