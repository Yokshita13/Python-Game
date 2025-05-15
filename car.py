import turtle

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(500)

myPen.color("#333333")

def clearScreen():
  myPen.penup()
  myPen.goto(0,0)
  myPen.setheading(0)
  myPen.clear()
  myPen.pendown()
  
def drawMercedesLogo():
  clearScreen()
  myPen.circle(100)
  myPen.left(90)
  myPen.penup()
  myPen.forward(100)
  myPen.pendown()
  myPen.forward(100)
  myPen.penup()
  myPen.forward(-100)
  myPen.left(120)
  myPen.pendown()
  myPen.forward(100)
  myPen.penup()
  myPen.forward(-100)
  myPen.left(120)
  myPen.pendown()
  myPen.forward(100)
  myPen.penup()
  myPen.forward(-100)
  myPen.left(120)
  
def drawAudiLogo():
  clearScreen()
  #Add your code here
  
def drawCitroenLogo():
  clearScreen()
  #Add your code here
  
def drawChryslerLogo():
  clearScreen()
  #Add your code here
  
def drawVolksWagenLogo():
  clearScreen()
  #Add your code here
  
#Main Program Starts Here
drawVolksWagenLogo()
drawChryslerLogo()
drawCitroenLogo()
drawAudiLogo()
drawMercedesLogo()
