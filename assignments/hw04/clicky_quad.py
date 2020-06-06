"""
clicky_quad.py
=====
Write a function that will complete the mostly written turtle program 
below. All of the turtle parts have been written for you; you will just
need to write one function. The completed program draws circles every 
time the user clicks on the screen. Each circle will be a different color
based on where the screen is clicked:

/http://foureyes.github.io/csci-ua.0002-spring2017-002-00://foureyes.github.io/csci-ua.0002-spring2017-002-008/resources/img/click-circles.gif

Check out the animated gif!

Again, the program is already mostly written for you. Just finish the 
function specified by "TODO:" in the comments below.
"""

import turtle
t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
t.hideturtle()
wn.tracer(0)

# set the width and height of our screen
width, height = 500, 500
wn.setup(width, height)

# TODO:
# Create a function called get_quadrant_color:
# 
# a. it should have two parameters, click_x and click_y
# b. the parameters represent the coordinates of where the mouse was when
#    when the screen was clicked
# c. the function should return a string representing one of the following
#    four colors: red, green, blue and yellow
# d. determine what color to give back based on what quadrant the user
#    clicked on:
#    * red - upper right
#    * green - lower right
#    * blue - upper left
#    * yellow - lower left
#
# YOU DO NOT HAVE TO CALL THE FUNCTION
#
# YOU CAN ASSUME THAT THE x and y COORDINATES WILL BE PASSED IN TO IT
# AUTOMATICALLY BY THE PARTS OF THE PROGRAM THAT ARE ALREADY WRITTEN
# =====================================

# (define get_quadrant_color here!)






def handle_click(x, y):
    # pick your pen up
    # =====================================
    t.up()

    # move your turtle to the x and y coordinates that are the parameters
    # of this function
    # =====================================
    t.goto(x, y)

    # put your pen back down
    # =====================================
    t.down()

    # call your get_quadrant_color function here and save save the result 
    # in a variable called quadrant_color
    # =====================================
    quadrant_color = get_quadrant_color(x, y)

    # set the turtle's drawing color to the quadrant_color variable that 
    # you created above
    # =====================================
    t.color(quadrant_color)

    # draw a filled circle by calling the following methods on your
    # *turtle object* in order:
    # 
    # begin_fill()
    # circle() <--- circle has radius as a parameter
    # end_fill()
    # =====================================
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# when the screen is clicked, call the handle_click function (and pass it the
# x and y coordinates
wn.onclick(handle_click)

wn.mainloop()

