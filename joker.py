import turtle
t = turtle.Turtle()

#draw the face outline
t.penup()
t.goto(0,-200)
t.pendown()
t.circle(200)

#draw the eyes
t.penup()
t.goto(-80,50)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(80,50)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

#draw the pupils
t.penup()
t.goto(-80,70)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(80,70)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

#draw the nose
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(90)
t.right(45)
t.forward(50)
t.left(135)
t.forward(100)

#draw the mouth
t.width(5)
t.penup()
t.goto(-40,-70)
t.pendown()
t.setheading(270)
t.circle(40,180)

#add some color
t.color('#ff69B4')#hot pink

#Draw the blush 
t.penup()
t.goto(-120,-20)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(120,-20)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

#hide the turtle and display the final image
t.hideturtle()
turtle.done()

        