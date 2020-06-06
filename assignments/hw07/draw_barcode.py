"""
draw_bardcode.py
=====
use your upc.py module to attempt to draw the barcode represented by your 
string of bar widths. The `prompt` function below will cause a window to 
open asking the user for a number. Draw the barcode associated with that number
if the number is a valid barcode number.
"""
import upc
import turtle

t = turtle.Turtle()
wn = turtle.Screen()

t.hideturtle()

# ask user for barcode number
prompt = 'Please enter a barcode number:'

########################
# your code goes here! #
########################


wn.update()
wn.exitonclick()

