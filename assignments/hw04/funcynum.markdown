---
layout: hw
title: funcynum.py
prefix: ../../
---

funcynum.py
=====

This file will contain functions that you'll use in feeling_quizzy.py. There
are 4 parts to this file, and they all depend on one another, so they must be 
done in order. The functions in this file will ultimately produce 'ASCII' art 
numbers. For example, the number 5:

{% highlight python %}
*****
*
*****
    *
*****
{% endhighlight %}


Part 1 - Create functions that make horizontal and vertical line strings 
-----
Create three functions:

1. __`horizontal_line(char, width, left_padding)`__:
    * __input__:
        * the character to make the line out of (`*` for example)
        * the total width of the line
        * the number of spaces before the line (left padding)
    * __processing__: 
        * creates a &lt;width&gt; wide string composed of the characters specified, 
          starting with an &lt;left_padding&gt; number of spaces 
    * __output__: 
        * __returns a string__ representing a horizontal line 

2. __`vertical_lines(char, height, left_padding, number, interior_offset)`__:
    * __input__:
        * the character to make the line out of (`*` for example)
        * the total height of the line
        * the number of spaces before the line (left padding)
        * the number of vertical lines to draw
        * the space between each line (an interior offset)
    * __processing__: 
        * creates a string that represents the specified number of vertical
          lines 
        * each line is &lt;height&gt; tall 
        * and is composed of the characters specified 
        * there are &lt;interior offset&gt; number of spaces between each vertical
          line
        * there is an &lt;left_padding&gt; number of spaces before the lines begin
        * for example, the string, `'* *\n* *\n* *\n* *'`, is a set of two vertical lines, 
          each 4 characters tall, with one space character between the lines, with no left padding. __NOTICE THAT THERE IS 
          NO NEW LINE__ at the end, and there __ARE NO TRAILING SPACES__
        * __YOU MUST USE NESTED LOOPS TO CONSTRUCT THIS STRING__
        * hint: the outer loop can represent row, the inner loop can represent
          column... and you can use the col_num or row_num to determine if an
          interior offset or newline should be added
    * __output__: 
        * __returns a string__ representing a series of vertical lines
        
3. __`vertical_line(char, height, left_padding)`__:
    * __input__:
        * the character to make the line out of (`*` for example)
        * the total height of the line
        * the number of spaces before the line (left padding)
    * __processing__: 
        * creates a &lt;height&gt; tall string composed of the characters specified, 
          starting with an &lt;left_padding&gt; number of spaces 
        * hint: imply call your vertical_lines function so that only 1 line is
          printed (remember to pass along the left_padding and character, though!)
    * __output__: 
        * __returns a string__ representing a single vertical line 

Examples:

{% highlight python%}
print(horizontal_line('*', 5, 0))

*****
{% endhighlight %}


<br>

{% highlight python%}
print(horizontal_line('+', 2, 4))

    ++
{% endhighlight %}

<br>

{% highlight python%}
print(vertical_line('*', 2, 5))

     *
     *
{% endhighlight %}

<br>

{% highlight python%}
print(vertical_lines('+', 4, 0, 5, 3))

+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
{% endhighlight %}


Part 2 - Create functions that print out the number 0 - 9, +, and -
-----
Create 12 additional functions that print out the numbers 0 - 9, +, and -. All
numbers will have a flexible width, but you can __assume that the HEIGHT OF THE
NUMBERS WILL ALWAYS BE 5__. Use the horizontal and vertical line drawing 
functions to write these functions.

The functions will be called print_one, print_two ... print_minus. The general 
input/output/processing chart will looks similar for each functions. Here's an
example input/output/processing chart, an actual function definition for the
function that prints out the number one, and some examples of usage:

__`print_one(char, width)`__

* __input__:  
    * a character to create the number with
    * the width of the number
* __processing__: 
    * __prints__ an 'ASCII' art number that's 5 characters tall and as wide as the
      argument passed in (<width> characters wide)
    * if a width is less than 3, default to 3
* __output__:     
    * __returns nothing (no return statement!)__

{% highlight python %}
def print_one(char, width):
    if width < 3:
        width = 3
    print(vertical_line(char, 5, width - 1))
{% endhighlight %}

Example Output (note the relationship between the number of leading spaces and
the total width):

{% highlight python %}
print_one('v', 5)
    v
    v
    v
    v
    v
{% endhighlight %}

<br>

{% highlight python %}
print_one('X', 3)
  X
  X
  X
  X
  X
{% endhighlight %}

<br>

{% highlight python %}
print_one('o', 1) # default to 3 width
  o
  o
  o
  o
  o
{% endhighlight %}

Here's an example of running all of the functions and the resulting output:

{% highlight python %}
print_zero('*', 5)
print()
print_one('*', 5)
print()
print_two('*', 5)
print()
print_three('*', 5)
print()
print_four('*', 5)
print()
print_five('*', 5)
print()
print_six('*', 5)
print()
print_seven('*', 5)
print()
print_eight('*', 5)
print()
print_nine('*', 5)
print()
print_plus('*', 5)
print()
print_minus('*', 5)

*****
*   *
*   *
*   *
*****

    *
    *
    *
    *
    *

*****
    *
*****
*
*****

*****
    *
*****
    *
*****

*   *
*   *
*****
    *
    *

*****
*
*****
    *
*****

*****
*
*****
*   *
*****

*****
    *
    *
    *
    *

*****
*   *
*****
*   *
*****

*****
*   *
*****
    *
    *

  *
  *
*****
  *
  *



*****
{% endhighlight %}

Part 3 - Create a function that checks an addition and subtraction operation
-----
Create a function called check_answer. It will will determine if a given 
addition or subtraction problem was solved correctly based on the operands, answer
and operator passed in. 

__`check_answer`__

* __input__:  
    * the 1st (or left) operand
    * the 2nd (or right) operand
    * the proposed answer
    * the operator... either + or -
* __processing__: 
    * runs the operator on the operands
    * checks against the proposed answer
    * if the operator isn't + or -, default to +
* __output__:     
    * __returns a boolean__ - `True` if the answer matches the actual result of the calculation
      ...returns `False` otherwise

Example usage and output:

{% highlight python %}
answer1 = check_answer(1, 2, 3, "+")
print(answer1)
answer2 = check_answer(1, 2, -1, "-")
print(answer2)
answer3 = check_answer(9, 5, 3, "+")
print(answer3)
answer4 = check_answer(8, 2, 4, "-")
print(answer4)
answer3 = check_answer(9, 5, 3, "*")
print(answer3)

True
True
False
False
False
{% endhighlight %}

Part 4 - Clean Up
-----
Clean up your finished file by doing the following:

* once you're certain that your functions are working the way you expect... 
* __COMMENT OUT ALL OF YOUR TEST CODE!__ (so that running your file does not
  produce any output - we'll see better ways of doing this later)   
* ensure that your file and functions are all named properly
* add comments to your file (including your name, section and date at the 
  beginning)

This will prep the file for the next file in the homework, feeling_quizzy.py,
and it will help with grading. 

Extra Credit
-----

1 point - move your test code so that it runs when you run the file, but
not when you import this as a module (relevant for feeling_quizzy.py)

* at the end of this file... add:

{% highlight python %}
#  this means... if this file is the actual file being run...
if __name__ == '__main__':
{% endhighlight %}

* ... within that if statement, add all of your test code
* when you run the file (funcynum.py), your test code will run
* however, if you import this as a module in another file, your test 
  code will not run

2 points - implement multiplication 

* add the multiplication sign (can be something that resembles an X or `*`)
* amend your check_answer so that `*` doesn't cause addition, but instead
  checks for multiplication

