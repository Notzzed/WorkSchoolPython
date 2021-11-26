from turtle import *

up()
goto(-500,0)
down()
color('blue')
for i in range(5):
    forward(100)
    left(72)

up()
goto(-300,0)
down()
color('red')
for i in range(5):
    forward(200)
    left(72)

up()
goto(50,0)
down()
color('purple')
for i in range(12):
    forward(50)
    left(30)

up()
goto(300,0)
down()
color('green')
for i in range(50):
    forward(5+i)
    left(36)

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
