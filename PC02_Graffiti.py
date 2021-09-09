#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Megan Dukek
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()
turtle.left(90)
turtle.forward(110)
turtle.left(90)
turtle.forward(95)
turtle.pendown()

turtle.pensize(5)
turtle.color("purple4")
turtle.begin_fill()
turtle.right(90)
turtle.forward(215)
turtle.right(135)
turtle.forward(215)
turtle.right(114)
turtle.forward(165)
turtle.end_fill()

turtle.penup()
turtle.right(130)
turtle.forward(110)
turtle.pendown

turtle.fillcolor("gold1")
turtle.begin_fill()
for i in range(5):
    turtle.forward(45)
    turtle.right(144)
    turtle.forward(45)
    turtle.right(72)

turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(70)
turtle.pendown

def smallStar():
    turtle.color("gold1")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
        turtle.forward(30)
        turtle.right(72)
        
    turtle.end_fill()

smallStar()

turtle.penup()
turtle.right(120)
turtle.forward(50)
turtle.pendown

smallStar()

turtle.penup()
turtle.goto(45,-65)
turtle.pendown()



turtle.pensize(10)
turtle.color("SaddleBrown")
turtle.right(150)
turtle.forward(40)

turtle.penup()
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.pendown()

turtle.color(255,255,0)
turtle.begin_fill()
for i in range(5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.goto(100,80)
turtle.pendown()
turtle.pensize(2)

def smallCircle():
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    
smallCircle()

turtle.penup()
turtle.goto(150,150)
turtle.pendown()

smallCircle()

turtle.penup()
turtle.goto(270,100)
turtle.pendown()
    
def largeCircle():
    turtle.speed(8)
    turtle.color("LightCyan")
    turtle.circle(40)
    
    turtle.right(10)
    
for i in range(70):
    largeCircle()




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
