from myFunctions import *
turtle.colormode(255)

turtle.tracer(0)
bob.speed(0)

bob.width(0)

#polygon
turtle.bgcolor("black")
for times in range(256):
    c = (255 - times, 0, times)#gradient colors
    color = c
    polygon(4, times * 2, 91, c)
    bob.left(15)

#jump
jump(0,0)#sets the turtle back to the middle(beginning)


#polygon2
for times in range(256):
    c = (times, 255-times, 0)#gradient colors
    color = c
    polygon2(4, times * 3, 92, c)




