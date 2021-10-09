#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:20:00 2021

@author: sazamore

A wraparound boundary, demonstrated with a ghost moving left
to right against a black background. Ghost crosses a boundary
10 times before stopping.
Edited by: Megan Dukek
Ghost crosses boundary 20 times before stopping-  *supposed* to move in a diamond shape. "Float" allows
a depiction fo the path the ghost has taken.
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================
ghost = turtle.Turtle(shape="circle")
size = 4
running = True # while loop conditional
step = 1 # increment of ball movement (controls speed of ghost)
count = 0 # edge crossingcounter, to determin when to stop animating
crosses = 15 # number of edge crosses to stop after

# import and set image as turtle shape
ghostImg = "ghostgif.gif" # turtle library ONLY works with gifs!
panel.addshape(ghostImg) # save the image to the panel so it knows what to draw
ghost.shape(ghostImg) # change the turtle shape to the saved image

ghost.up() # drawing to see float
ghost.up() # drawing to see float
ghost.color("pale turquoise")

# ================ FUNCTION DEFINITION =========================
def float():
    '''Will send the ghost in a circle'''
    for i in range(5):
        ghost.circle(10)
        ghost.forward(5)
    
# ================ ANIMATION LOOP =========================
while running:
    ghost.down() # drawing to see float
    float()
    ghost.up()
    #ghost.forward(step) # move ghost
    xpos = ghost.xcor() # get x position
    ypos = ghost.ycor() # get y position
         
    if xpos >= w/2:
        # check if it crosses the RIGHT edge
        ghost.goto(0,h/2) # move it to the top edge
        ghost.right(140) # have to change angle of ghost otherwise it will keep moving horizontal. 
        count += 1 # keep track of the crossing
        
    if ypos >= h/2:
        # check to see if it cross top edge
        ghost.goto(-w/2,0) # move to left edge
        ghost.right(45)
        count += 1
        
    if xpos <= -w/2:
        # check if it crosses the LEFT edge
        ghost.goto(0,-h/2) # move it to bottom edge
        ghost.right(45)
        count += 1
        
    if ypos <= -h/2:
        # check if it crosses the bottom edge
        ghost.goto(w/2,0) # move it to the right edge
        ghost.right(45)
        count += 1 # keep track of the crossing
         
         
    if count > crosses:
        # check if we've made the intened number of crosses
        running= False    
        
    panel.update() # update the window with everything drawn in a single frame
    
# CLEANUP
turtle.done()



