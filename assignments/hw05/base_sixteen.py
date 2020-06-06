"""
base_sixteen.py
=====
Write a function, convert, that takes a base 16 number and returns its base 10
value (decimal value).

The digits in a base 16 number can be 1 of 16 possible values:

* 0 - 9 represents the numbers 0 through 9
* A - F represents the numbers 10 through 15

The right-most digit is the 1's place (16 ** 0), the next place to the left is
the 16's place (16 ** 1)... with the exponent increasing with each place to 
the left.

An example is:

1AC
-----
(1 * 16 ** 2) + (10 * 16 ** 1) + (12 * 16 ** 0)

256 + 160 + 12

428

In some programming languages, a base 16 number is prefixed with an 0x to 
specify that the remaining "digits" are part of a base 16 number rather than
a different base (like base 10). For example:

1AC would be represented as 0x1AC

The convert function will:

* take a string that represents a base 16 number prefixed with 0x. 
* it will return the base 10 value of the number as an int
* if the original number is not valid (that is, it has characters
  other than 0 - 9, A - F, a - f, or it does not start with 0x)... 
  then `return None`
* lowercase letters are treated as their uppercase equivalent (for
  example, a is 10, b is 11, etc.)
* the 0x prefix can be ignored as part of the calculation of the 
  value of the base 16 number
* the incoming base 16 number can be any length

Here are some example calls to the convert function:

print(convert('0x0001')) # 1
print(convert('0x0010')) # 16
print(convert('0x21')) # 33
print(convert('0xAE')) # 174
print(convert('0x7BF5')) # 31733
print(convert('0x7bf5')) # 31733
print(convert('2AF3')) # None
print(convert('0xZZZ')) # None
"""
