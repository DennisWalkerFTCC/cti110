# Creating shapes using turtle
# 9/12/19
# CTI-110 P2HW2 - Turtle graphic
# Dennis Walker

""" PseudoCode """
# import turtle
# create a turtle and turtle window
# End goal: use the turtle to create a 3D Rectangular prism
# Position the turtle then create a 100 pixel line
# Position turtle to the left and create a 100 pixel line
# Position turtle 135 degrees, then create a 141 pixel line
# A triangle has been created, position turtle 45 degrees right
# Create a 100 pixel line, then angle 135 degrees right
# Create a 141 pixel line, then angle right 45 degrees
# create a 100 pixel line, a 3D cheese wedge has been created
# Angle 135 degrees, then take the previous path of 141 pixel line
# angle right again 135 degrees. create a 100 pixel line
# turn left 135 degrees, create a 142 pixel line
# turn left 45 degrees, create a 100 pixel line
# turn left 90 degrees, create a 100 pixel line
# turn right 180 degrees, take the path backwards
# turn left 135 degrees, go forward 142 pixels
# take a break from monitoring the turtles moves
# turn left 135 degrees, create a 100 pixel line
# turn left 45 degrees, travel 142 pixel line
# put pen up
# travel 100 pixels forward, the shape is now done
# wait for the user to close the window

import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()


turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(135)
turtle.forward(141)
turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(141)
turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(141)
turtle.right(135)
turtle.forward(100)
turtle.left(135)
turtle.forward(142)
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
turtle.left(135)
turtle.forward(142)
turtle.left(135)
turtle.forward(100)
turtle.left(45)
turtle.forward(142)
turtle.penup()
turtle.forward(100)

wn.mainloop()
