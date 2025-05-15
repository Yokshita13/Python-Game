#rainbow in benzene
import turtle
colors = ['violet','indigo','blue','green','yellow','orange','red']
t = turtle.Turtle()
turtle.bgcolor('black')
for i in range (360):
    t.pencolor(colors[i%6])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)
    
