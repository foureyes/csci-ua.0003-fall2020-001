"""
slashes.py - 5 points
=====

Write a program that asks for a height and width, and prints out a pattern
based on that height and width.  You __MUST__ use nested loops to do this.  
See the pattern below.

Example Output:
width:
> 5
height:
> 5
|///|
|\\\|
|///|
|\\\|
|///|

width:
> 3
height:
> 3
|/|
|\|
|/|

Hints:
* accumulate characters into an empty string variable
* the rails can be implemented by testing which column you're on (1st or last)
* modulo may be useful for alternating slashes
* go to a new row / new line by appending the new line character (\n)
* again, use nested loops to do this
"""
