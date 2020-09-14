'''
prime_time.py
=====

PART 1
------

In `prime_time.py`...

1. __COMMENT YOUR SOURCE CODE__  
  * add the following to the top of your file in a multiline comment (`""" multiline """`)
    * the homework number: "Homework #01"
    * the class number, section, and semsester: CSCI-UA.0003-001 Fall 2020
    * your name: "Carol Coder"
    * your net id: "abc123"
    * the date in YYYY-MM-DD: "2020-01-01"
    * for example:
      ```
Homework #01
CSCI-UA.0003-001 Fall 2020
Carol Coder
abc123
2020-01-01
```
  * in comments interspersed in your code...
    * briefly describe parts of your program that aren't self-explanatory
    * no need to add superfluous comments
2. Write a program that does the following:
  * starts by printing out: `Part 1`
  * asks the user for a number: `Give me a whole number`
    * it's ok to assume that the user will enter a whole number (no need to handle invalid input)
  * prints out a table of that number multiplied by the following prime numbers:  
    * ...`3, 5, 7, 11`
    * each row / line in the table should be `$USER_NUMBER * $PRIME_NUMBER = $RESULT`, where
      * `$USER_NUMBER` is the number entered by the user
      * `$PRIME_NUMBER` is `3, 5, 7, 11`
      * `$RESULT` is the product of the number entered by the user and one of the prime numbers
3. Example interaction (the number after `>` is user input):
  ```
Part 1
Give me a number
> 17
17 * 3 = 51
17 * 5 = 85
17 * 7 = 119
17 * 11 = 187
17 * 127 = 2159
```

PART 2 
------

__Modify the original program__ so that

1. It will format the output so that the original number and the prime number are left aligned and the product is right aligned
  * that is, the left-most part is aligned on the left
  * the right-most part, the result, is aligned evenly on the right
2. ⚠️ It's ok to assume that  __the user will enter either a 1 or 2 digit number__
3. Do this without using if statements
4. Big hint: it's helpful to use `format` to control the width of the left and right parts of the table... or optionally, use `len`
5. Example interaction (everything after `>` is user input); __pay close attention to alignment__ :
  * Run 1: user enter 17
    ```
Part 2
Give me a number
> 17
17 * 3   =   51
17 * 5   =   85
17 * 7   =  119
17 * 11  =  187
17 * 127 = 2159
```
  * Run 2: user enters 20 (note the difference in spacing)
    ```
Part 2
Give me a number
> 20
20 * 3   =   60
20 * 5   =  100
20 * 7   =  140
20 * 11  =  220
20 * 127 = 2540
```
  * Run 3: user enters 9 (note the difference in spacing)
    ```
Part 2
Give me a number
> 9
9 * 3   =   27
9 * 5   =   45
9 * 7   =   63
9 * 11  =   99
9 * 127 = 1143
```

PART 3 (Optional)
------

__Modify the original program__ so that

1. Any number can be put in, and the spacing will adapt appropriately
2. You don't have to account for wrapping if the line is longer than the screen
3. Example interaction (the number after `>` is user input); __pay close attention to alignment__ :
  * Run 1: user enters 123
    ```
Part 3
Give me a number
> 123
123 * 3   =   369
123 * 5   =   615
123 * 7   =   861
123 * 11  =  1353
123 * 127 = 15621
```
  * Run 2: user enters 789
    ```
Part 3
Give me a number
> 789
789 * 3   =   2367
789 * 5   =   3945
789 * 7   =   5523
789 * 11  =   8679
789 * 127 = 100203
```
'''
