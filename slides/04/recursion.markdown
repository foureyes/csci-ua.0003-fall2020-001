---
layout: slides
title: "A Brief Look at Recursion "
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Recursion

__Recursion__ is a process of repeating something in a self similar way.  When we define a __recursive function__, we define a function in terms of itself.  That is, it can call itself to define itself!

A couple of examples where we'll use recursion are:

* an approach to generating a mathematical sequence or computing a mathematical operation 
* generating a fractal

</section>

<section markdown="block">
## Fractals

You know... fractals!

* [Classic](https://www.nsf.gov/news/mmg/mmg_disp.jsp?med_id=51856&from=)
* [Pizza Pizza](https://ny.eater.com/2015/5/29/8687941/vinnies-pizzeria-pizza-on-pizza-slice)
* [The Largest Island in a Lake...](http://www.elbruz.org/islands/Islands%20and%20Lakes.htm), and updated on [wikipedia](https://en.wikipedia.org/wiki/Recursive_islands_and_lakes)
* [Gosling / Culkin](https://external-preview.redd.it/niZFU1ETuVUPW_Z6sUuwyVsMNBqertfE9F5Ev-kI3qw.jpg?auto=webp&s=fe37390400d32a67c89acbbd86021662026c932a) 
</section>

{% comment %}
<pre><code data-trim contenteditable>

</code></pre>
{% endcomment %}
<section markdown="block">
## Back to Recursion

So... to create a recursive function definition:

* you'll need to create a function that calls itself
* a way for the function to stop calling itself (sometimes called a base case)
* otherwise... __what do you think will happen here?__

<pre><code data-trim contenteditable>
def is_this_forever():
	print("yes")
	is_this_forever()

is_this_forever()
</code></pre>
{:.fragment}

RuntimeError: maximum recursion depth exceeded while calling a Python object
{:.fragment}
</section>

<section markdown="block">
## Factorial Revisited

If we look at factorial again....

* 5! = 5 * 4 * 3 * 2 * 1
* can be rewritten as: 5 * 4!
* we can define factorial in terms of itself!
* (note that 0! is 1)

</section>

<section markdown="block">
## Factorial Using Recursion

__Let's try to reimplement factorial using recursion rather than a loop. &rarr;__

* we'll need to call the function within its definition
* we may need an end condition

<pre><code data-trim contenteditable>
def factorial(n):
	if n != 0:
		return n * factorial(n-1)
	else:
		return 1

print(factorial(0))
print(factorial(2))
print(factorial(3))
print(factorial(5))
</code></pre>
{:.fragment}
</section>
<section markdown="block">
## Asking Using Recursion

__Let's try to reimplement a program that continues to ask a question until the user says no by using recursion rather than a loop (how does the loop version go again?). &rarr;__

<pre><code data-trim contenteditable>
Type "no" to stop
> yup
Type "no" to stop
> no
</code></pre>

<pre><code data-trim contenteditable>
def ask_for_input():
    if input("Type \"no\" to stop\n> ") != "no":
        ask_for_input()
    else:
        # else is not necessary, but left in for clarity
        return

ask_for_input()
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## A Tree

__Let's try to draw a tree using recursion. &rarr;__

<pre><code data-trim contenteditable>
import turtle

leo = turtle.Turtle()
wn = turtle.Screen()
def branch(t, length, length_multiplier, min_length):
	if length < min_length:
		return
	else:
		t.forward(length)
		t.left(30)
		branch(t, length * length_multiplier, length_multiplier, min_length)
		t.right(60)
		branch(t, length * length_multiplier, length_multiplier, min_length)
		t.left(30)
		t.back(length)
		return
# base - branch(leo, , 0.6, 10)
branch(leo, 80, 0.6, 10)
wn.mainloop()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## More Trees

<pre><code data-trim contenteditable>
import random
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)

t.left(90)

"""
add functions here
draw_tree
forest
"""

forest()
wn.mainloop()

</code></pre>



</section>

<section markdown="block">
## draw_tree

<pre><code data-trim contenteditable>
def draw_tree(s, w):
    if s <= 5:
        return
    else:
        new_w = w if w <= 1 else w - 1
        t.pensize(w)
        a1 = random.randint(20, 50)
        t.forward(s)
        t.left(a1)
        draw_tree(s - random.randint(2, s // 2), new_w)
        a2 = random.randint(20, 50)
        t.right(a1 + a2)
        draw_tree(s - random.randint(2, s // 2), new_w)
        t.left(a2)
        t.back(s)
</code></pre>

</section>

<section markdown="block">
## forest

<pre><code data-trim contenteditable>
def forest():
	for x in range(-300, 301, 200):
    	print(x)
    	t.up()
    	t.goto(x, -100)
    	t.down()
    	t.color("#{}".format(str(random.randint(0, 6)) * 3))
    	draw_tree(random.randint(30, 100), random.randint(4, 10))
</code></pre>
</section>
