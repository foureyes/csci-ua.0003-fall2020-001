"""
snake_eyes.py (8 points)
=====

Write a program that simulates rolling 2 6-sided repeatedly. It will keeping 
track of when the result of both rolls is 1 (snake eyes). The program will 
count the number of rolls it took to get snake eyes. 

The program will repeat this process 100 times... keeping track of the total 
number of rolls.  Once the 100 trials have been exhausted, the program will 
print out the average number of rolls that it took to get snake eyes (consider 
what you think this average should be).

* you __MUST__ use nested loops for this program
    * one loop, the outer loop,  will repeat the process 100 times
    * the other loop, the inner loop, will continue rolling until a 2 is rolled
      (both dice are 1)
* do the following 100 times (this should be your outer loop):
    * print out the trial number (it should be from 1 up-to and including 100)
    * roll 2 6-sided dice repeatedly (this should be your inner loop)
	* print out the result of each roll
	* keep track of the number of rolls
	* stop when both dice are 1 (snake eyes)
	* print out the total number of rolls it took to get snake eyes
	* add that to a running total (so that you can get an average later)
* print out the average number of times it took to roll a snake eyes
    * round the average using the built-in round function
* example output:

trial 1:
6, 3
1, 5
4, 2
4, 6
3, 3
5, 4
6, 6
3, 6
4, 3
2, 3
3, 5
6, 4
3, 1
3, 5
5, 3
6, 5
1, 1
=====
17 rolls

.
.
(trials 2 through 99)
.
.

trial 100:
5, 6
5, 4
4, 6
1, 1
=====
4 rolls

average: 37
"""
