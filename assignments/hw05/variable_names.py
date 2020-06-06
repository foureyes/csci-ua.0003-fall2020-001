"""
variable_names.py
=====
You're tired of inadvertently writing Python variable names that aren't valid,
so you decide to write a program that checks the validity of variable names. 

To write this program, you'll create a function called is_valid_name. Your 
program will then continually ask the user for a variable name, and you'll use 
your function to determine whether or not it's valid. If the user enters an 
invalid variable name 3 times in a row or if they enter a valid name, stop 
asking for a variable name! 

a) Create a function called is_valid_name
   * parameters: a string representing a variable name 
   * body: use the rules below to determine whether or not the variable is 
     valid 
   * return: either true or false depending on whether or not the variable 
     name is valid 
b) A valid variable name:
   * starts with only an underscore or a letter
   * is only composed of underscores, letters or numbers 
c) Within an conditional at the end of your function, write your program...
    if __name__ == '__main__':
        # your program goes here
d) Continually ask the user for a variable names
e) Use your function to check if it's valid
f) If  the user enters a valid name... or if they enter 3 invalid names, stop asking
       
Example usage of function:
-----
print(is_valid_name('1asdf')) # False
print(is_valid_name('#foo'))  # False
print(is_valid_name('asdf1')) # True
print(is_valid_name('_foo'))  # True
print(is_valid_name('f_oo'))  # True

Example Interaction of program that uses above function:

Variable name plz
> $hello
Variable name plz
> hello
"""
