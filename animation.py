# animation in python using tuttle library

import turtle
turtle.bgcolor("lightgreen")
turtle.pensize(1.6)
turtle.speed(0.5)

color= {"red","blue","orange","purple"}

for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(120)
        turtle.left(10)


turtle.mainloop()