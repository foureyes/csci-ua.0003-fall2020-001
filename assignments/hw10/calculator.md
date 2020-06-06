---
layout: homework
title: calculator.py
---
<link href='https://fonts.googleapis.com/css?family=Merriweather:400,700,400italic,700italic' rel='stylesheet' type='text/css'>


# Stack, RPN Calculator, and Animation (Homework and Extra Credit for Midterm\*)


<pre><code data-trim contenteditable>   ____________________
 /____________________/|
|  _________________  ||
| |       2 8 + 5 * | ||
| |_________________| ||
|  __ __ __ __ __ __  ||
| |__|__|__|__|__|__| ||
|  ___ ___ ___   ___  ||
| |_7_|_8_|_9_| |_+_| ||
| |_4_|_5_|_6_| |_-_| ||
| |_1_|_2_|_3_| |_x_| ||
| |_._|_0_|_=_| |_/_| ||
|_____________________|/
</code></pre>
{%comment%}_ {%endcomment%}

\* additional 4 points to lower scoring midterm 

### Overview

Create a class, `RPNCalculator`, that can evaluate a [reverse polish notation (postfix) mathematical expression](http://en.wikipedia.org/wiki/Reverse_Polish_notation). Implement your `RPNCalculator` class by creating and using a `Stack` class - a data structure similar to a list, but with operations and methods supporting _stack_ like functionality.

### Setup

Create 4+ classes: 

1. <code>Stack</code> in `stack.py`  (homework)
2. <code>RPNCalculator</code> in `calculator.py` (homework)
3. two classes of _your choice_ in <code>animation.py</code> (extra credit)


### ⚠️ Submission / Scoring

{% comment %}
* If your second midterm's raw score was __not__ 10% higher than your first midterm's raw score, the extra credit will count for up-to 4 additional points to your lowest scoring midterm grade.
* There will be two assignments on NYU Classes:
	1. upload `stack.py` and `calculator.py` to Homework 10
	2. upload `animation.py` to Extra Credit
{% endcomment %}

### Part 1: Stack Class (Homework)

__Create a class, `Stack` that represents a [data structure called a stack](http://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29)__

* a stack allows you to store elements by _pushing_ items on to the stack of elements
* ... and retrieve and remove items by _popping_ them off of the top of the stack
* create your own `Stack` class
* this will seem very similar to a list, but instead, but it will support different methods / operations
* 👀 internally, you can store the data as a list! (that is, when a stack is first created, create an instance attribute that's set to an empty list)
* your <code>Stack</code> class should support:
	* <code>__str__</code> &rarr; returns a <code>str</code> representation of the `Stack` instancej0
	* <code>empty()</code> &rarr; returns a <code>bool</code> that describes whether or not the stack is empty
	* <code>peek()</code> &rarr; returns any type... allows you to "view" the value at the top of the stack without removing it
	* <code>push(value)</code> &rarr; does not return a value... however, adds _some value_ to the top of the stack
	* <code>pop()</code> &rarr; removes the top element (that is, the most recently added) element from the top of the stack... and returns it  (pretty much same as list method, `pop`)
* all of these operations should work on the internal list containing `Stack` instance's data
	* for example, `peek` will return the last element of the list if it exists
	* `push(value)` will simply append `value` to the list
	* `pop` can pretty much just call `pop` 😲 (as long as there are elements in the list)
	* `empty` will just return `True` or `False` depending on the length of the list (0 means empty, of course!)
	* <code>__str__()</code> should return a <code>String</code> representation of your stack (that is, it should _return_ a <code>str</code>)
		* when printed, the string should look like this (assuming 3 elements, with the number 3 as the last element pushed on the stack)
			```
|3|
|2|
|1|
 ‾ 
``` 
		* ⚠️ note that the character on the bottom of the stack is `‾` (&larr; copy and paste this into your text editor)
	* example usage of the `Stack` class:
		<pre><code data-trim contenteditable># create a new stack
s = Stack()
&nbsp; 
# check if it's empty by calling the empty method
print(s.empty()) # True
&nbsp; 
# add some values to the top of the stack by using push
s.push(1)
s.push(2)
s.push(3)
&nbsp; 
# take a look at (but don't remove) the first element with peek
print(s.peek()) # 3
&nbsp; 
# remove and return the most recently pushed element with pop
val = s.pop()
print(val) # 3
print(s)
# |2|
# |1|
#  ‾ 
</code></pre>

__Testing your code__

1. ⚠️  Make sure to name your classes and methods exactly as they appear in the instructions above
2. `stack.py` has some example code that prints out stack usage
3. Once your satisifed with your implementation, run `test_stack.py` to run automated tests (you can view the code in `test_stack.py` to see what features of your class are being tested
	* note that in some editors, like PyCharm, this may show up as `Run Unittests in...`
4. For simplicity, grading will be based solely on these automated tests
5. If your class fulfills the requirements, you should get output similar to this:
	```Ran 5 tests in 0.041s
&nbsp;
OK
&nbsp;
Process finished with exit code 0
```
6. An exception will occur if any of the tests fail
7. Some example of interpreting exceptions and failing tests include
	* the expected value was 10, but 5 was returned
		<pre><code data-trim contenteditable>10 != 5.0
&nbsp;
Expected :5.0
Actual   :10
&nbsp;
AssertionError: 5.0 != 10
</code></pre>
	* the string returned is not equal to the string expected (in particular, `|2|` should have been on top, and no `|2|` should be on the bottom)
		<pre><code data-trim contenteditable>|2|
|1|
 ‾ != |1|
|2|
&nbsp;
AssertionError: '|1|\n|2|\n ‾' != '|2|\n|1|\n ‾'
+&nbsp;|2|
&nbsp;&nbsp;|1|
-&nbsp;|2|
&nbsp;&nbsp;&nbsp;‾
</code></pre>

### Part 2: RPNCalculator Class (Homework)

Your <code>RPNCalculator</code> class should have the following constructor, methods and attributes 

* to create an instance of calculator: `RPNCalculator(expression)`, 
	* `expression` is a string representing a mathematical expression in Reverse Polish Notation (RPN)
	* each "token" in the string will be separated by a space
	* it will consist of numbers and operators
	* for example: `6 2 /`
* an attributes, `expression` should contain the original RPN expression passed in 
* a method, `evaluate()` should return the result of evaluating the saved RPN expression
* the algorithm for evaluating an RPN expression is as follows:
	<pre><code data-trim contenteditable>for token in expression
  if token is numeric
    push token on stack
  else if token is an operator
    pop the number of operands that operator takes off of the stack
	apply the operation on the operands
	push the new value on to the stack
if there's only one value left in the stack
  use that as the result of the calculation 
otherwise
  ...give back None
</code></pre>
* here is a sample run using the expression <code>23 7 + 2 *</code>:
	<pre><code data-trim contenteditable>token: '23', 23 is pushed on to the stack, stack = 23.0 
token: '7', 7 is pushed on to the stack, stack = 23.0 7.0 
token: '+', + pops 23 and 7, adds them and pushes 30.0 on to the stack, stack = 30.0 
token: '2', 2 is pushed on to the stack = 30.0 2.0 
token: '*', * pops 30 and 2 off of the stack, multiplies them and pushes 60 on to the stack, stack = 60.0 
result of calculation is 60
</code></pre>
* assume all operators (addition, multiplication, subtraction, division, and exponentiation) have two operands (so two elements will be popped off of the stack when you encounter an operator
* ⚠️ any non-numeric input should be considered an operator
* ⚠️ if an operator isn't supported, simply move on to the next token

__Testing your code__

1. ⚠️  Again, make sure to name your classes and methods exactly as they appear in the instructions above
2. `calculator.py` has some example code that prints out `RPNCalculator` usage
3. Once you're satisifed with your implementation, run `test_calculator.py` to run automated tests (you can view the code in `test_stack.py` to see what features of your class are being tested
	* note that in some editors, like PyCharm, this may show up as `Run Unittests in...`
4. For simplicity, grading will be based solely on these automated tests
5. If your class fulfills the requirements, you should get output similar to this:
	<pre><code data-trim contenteditable>Ran 4 tests in 0.041s
&nbsp;
OK
&nbsp;
Process finished with exit code 0
</code></pre>
6. An exception will occur if any of the tests fail

### Part 3: Animation(Extra Credit)

Up to 4 points extra credit on lower scoring midterm.

1. (+2) create at least two classes representing a drawing in turtle
	* for example a, `Tree` class... or a `Car` class  with x and y coordinates, a color attribute, a size attribute, etc.
	* ...and some methods, such as a `move` to change coordinates or `draw` ... so that it can draw itself on screen as a triangle on top of rectangle
	* the classes can have similar attributes and / or methods
	* one class can inherit from another class
2. (+1) create multiple instances of each class 
	* at least two for each)
	* each instance should be used to inform what is drawn on screen 
	* for example, two instances of a `Planet` class would result in two planets drawn on screen (hopefully using the instance's attributes to influence the drawing in _some_ way
4. (+1) finally, using [these slides](../../slides/turtle/turtle-more.html#48), incorporate animation into your project... at least one of your drawings should move in some way

