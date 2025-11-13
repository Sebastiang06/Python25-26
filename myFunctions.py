import turtle
bob = turtle.Turtle()

#polygon
def polygon(sides, distance, angle, color):
  for times in range(sides):
    bob.pencolor(color)
    bob.forward(distance)
    bob.left(angle)

#jump 
def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

#polygon2
def polygon2(sides, distance, angle, color):
  for times in range(sides):
    bob.pencolor(color)
    bob.forward(distance)
    bob.left(angle)

