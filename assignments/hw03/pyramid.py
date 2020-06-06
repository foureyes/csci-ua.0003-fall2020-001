"""
pyramid.py
=====

A Pyramid of Numbers
-----

Write a program that creates a pyramid of numbers with the left side of 
the pyramid counting down, and the right side of the pyramid counting
up. Note the alignment of the numbers.

Requirements
-----
* Ask the user for a number
    * You can assume the input is a valid integer
    * However, if it's 0 or less, ask for the height again
* Generate a pyramid made of numbers based on user input …
* Mimic the pyramid in the example output below
* Ensure that the spacing between each number is consistent
* It may be useful to widen the output window (make it horizontal)
* Hint: nested loops may be helpful
* Hint: if you need it, there's a built in function to calculate absolute value: abs
    * abs(-5) # returns 5
* Hint: some of these string related operators and functions may be helpful: 
    * repetition operator
    * format function
    * len function
    * str function

Example 1:
-----
Enter the height of your pyramid △
>-2
Enter the height of your pyramid △
>-5
Enter the height of your pyramid △
>3
      1     
    2 1 2   
  3 2 1 2 3 

Example 2:
-----
Enter the height of your pyramid △
>12
                            1
                          2 1 2
                        3 2 1 2 3
                      4 3 2 1 2 3 4
                    5 4 3 2 1 2 3 4 5
                  6 5 4 3 2 1 2 3 4 5 6
                7 6 5 4 3 2 1 2 3 4 5 6 7
              8 7 6 5 4 3 2 1 2 3 4 5 6 7 8
            9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9
         10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10
      11 10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 11
   12 11 10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 11 12
"""
