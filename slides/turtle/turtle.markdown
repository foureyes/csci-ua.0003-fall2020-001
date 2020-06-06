---
layout: slides
title: Turtle Graphics 
---
<section markdown="block" class="title-slide">
#  Turtle Graphics
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Turtle

__turtle__ is a Python module for drawing!

* you have a pen, called a "turtle"
* you give commands to your turtle, such as:
	* move forward
	* put the pen down
	* etc.

</section>


<section markdown="block">
## An Example

This draws a short horizontal line:

<pre><code data-trim contenteditable>
{% include classes/13/hello.py %}
</code></pre>
</section>

<section markdown="block">
##  The "Canvas" / Window

At the beginning of your turtle program...

* the "pen" (turtle / small triangle) starts at the center (0, 0)
* the turtle is facing right (imagine that it's looking east)

</section>


<section markdown="block">
## In Detail

bring in the turtle module

<pre><code data-trim contenteditable>
import turtle
</code></pre>

create a Screen object (this provides a canvas to draw on, and some window related commands)

<pre><code data-trim contenteditable>
wn = turtle.Screen()
</code></pre>

create a Turtle object to draw with

<pre><code data-trim contenteditable>
leo = turtle.Turtle()
</code></pre>
</section>

<section markdown="block">
##  ...Continued

tell the turtle to move forward 200 pixels

<pre><code data-trim contenteditable>
leo.forward(200)
</code></pre>

prevent the window from closing by calling `main loop`
<pre><code data-trim contenteditable>
wn.mainloop()
</code></pre>
</section>


<section markdown="block">
##  Basic Turtle Methods

These are all methods that you can call on your __Turtle__ object.

* __forward__(_distance_) - move the turtle forward by the specified _distance_
* __right__(_angle_) - turn the turtle right by _angle_ degrees
* __left__(_angle_) - turn the turtle left by _angle_ degrees
* __back__(_distance_) - move the turtle back by the specified _distance_

<pre><code data-trim contenteditable>
t.forward(200)
t.right(45)
</code></pre>
</section>


<section markdown="block">
##  Screen and Pen Drawing Attributes

Methods you can call on your __Turtle__ object:

* __color__(_colorstring_) - change the color of your _pen_ to _colorstring_, which can be "red", "green", etc.
* __pensize__(_size_) - change the size of your pen to _size_

<pre><code data-trim contenteditable>
t.color("blue")
</code></pre>

Methods you can call on your __Screen__ object

* __setup__(width, height) - window dimensions (default is 50% and 75% of screen)
* __bgcolor__(_colorstring_) - change the background color of your window to _colorstring_

<pre><code data-trim contenteditable>
wn.bgcolor("pink")
</code></pre>
</section>

<section markdown="block">
##  Color, Background and Pen Size
<pre><code data-trim contenteditable>
{% include classes/13/color.py %}
</code></pre>
</section>

<section markdown="block">
##  Moving Without Drawing

Methods you can call on your __Turtle__ object:

* __up__() - pick the pen up so that the turtle object doesn't draw when it moves
* __down__() - put the pen down so that the turtle object draws when it moves
<pre><code data-trim contenteditable>
t.up()  # picks the pen up, doesn't draw when the turtle moves
</code></pre>
</section>


<section markdown="block">
##  Pen Up, Pen Down

__BTW... what do you think this draws? &rarr;__

<pre><code data-trim contenteditable>
{% include classes/13/pen.py %}
</code></pre>
</section>

<section markdown="block">
##  Going Somewhere?

A method you can call on your __Turtle__ object:

__goto__(_x_, _y_) - move the turtle to the specified coordinates ..._x_ and _y_.  Note that if the pen is down, it will draw up to that coordinate.

<pre><code data-trim contenteditable>
t.goto(200, 200)  # picks the pen up, doesn't draw when the turtle moves
</code></pre>
</section>

<section markdown="block">
##  Goto

__BTW... what do you think this draws? &rarr;__

<pre><code data-trim contenteditable>
{% include classes/13/goto.py %}
</code></pre>
</section>

<section markdown="block">
## In Circles


__Draw a circle by calling `circle` and passing in a `radius`__

<pre><code data-trim contenteditable>
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.circle(50)

wn.mainloop()
</code></pre>

[See the docs](https://docs.python.org/3/library/turtle.html#turtle.circle) for more info and parameters (drawing a semicircle, for example)

</section>

<section markdown="block">
## Color

__Several methods must be used to fill in a shape with a color:__ &rarr;

<pre><code data-trim contenteditable>
# assuming surrounding setup code

# two arguments to color set both the pen and the fill
t.color("black", "red")

# surround shape with begin_fill() and end_fill()
t.begin_fill()
t.circle(80)
t.end_fill()
</code></pre>

</section>
