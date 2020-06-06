"""
automobile_costs.py (4 points)
=====
This program is variation of problem #4 in Programming Exercises for Chapter 5in Starting Out With Python.

Write a program that asks the user to enter the monthly costs for the 
following expenses incurred from operating his or her automobile: loan 
payment, insurance, gas, and oil.  The program should then display the total
monthly cost of these expenses and the total annual cost of these expenses.

For this exercise:

* create two functions: 
  * create a function called display_monthly_cost; it should take four inputs,
    each named after the specific expense (loan_payment, insurance, etc.)
  * create a function called main; it should take no inputs
* main will be responsible for:
  * asking for data from the user 
  * converting each value to an int
  * it should call the display_monthly_cost function with the values that it
    has converted
* display_monthly_cost will:
  * sum all of the values passed in to calculate and display a total monthly
    cost
  * it should then calculate and display a yearly cost
* call the main function at the end of your program (after you've defined your
  main function)
  
Example Output - Everything after the greater than sign (>) is user input:

Please enter the number of dollars spent every month for...
loan payment
> 500
insurance
> 50
gas
> 100
oil
> 0
======
Your total monthly cost is $650
Your total yearly cost is $7800
"""
