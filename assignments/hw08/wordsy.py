"""
wordsy.py
=====

Write a program that:

* asks the user a set of letters
* prints out all of the combinations of letters that make valid words __in 
  alphabetical order__
    * by using a dictionary file of words
    * and an algorithm specified in the instructions below
* see example output at end

Do this by:

* first downloading a dictionary of words:
    * http://foureyes.github.io/csci-ua.0002-fall2015-008/homework/hw09/enable1.txt
    * go to File --> save as ... to save the file in the same directory as 
      your Python program
* creating a function called find_words
    * it should have two parameters: 
        * a string representing the set of letters to build words from
        * a string that's the name of a dictionary file that contains
          all possible words
    * it should open the dictionary file
    * ...and find valid words that can be formed from the set of letters
    * it should return a list of valid words
* then... create another function, called main (this will be called later
  within an if statmement)
    * it should have no parameters
    * it should have no return value
    * it will ask the user for a set of letters that are between 1 and 7 
      characters long (inclusive)
        * if the input is not all letters
        * or if the input isn't at least one letter or is more than 7 letters
        * ... ask for input again
    * it will then ask the user for the maximum number of words to display
        * use try / except to deal with non-numeric input
        * if the user enter's non numeric input, just show all of the results
    * use the find_words function on the user input to get a list of valid
      words
    * print out the result in alphabetical order
    * only display, at most, the max number of words entered by the user
    * call main at the end of the program as follows:

# CALL YOUR main FUNCTION WITHIN THIS CONDITIONAL:

if __name__ == "__main__":
    main()

* use this algorithm to determine the valid words that can be formed from a 
  set of letters:
    * create a list of found words (there shouldn't be any words there yet!)
    * go through every word in your dictionary (that is, every line):
        * get rid of any leading or trailing white space with strip
        * create a temporary list out of the characters in the set of letters
          passed in to the function (do this to allow "removal" of characters)
            * create the temp list by using the built in function: list
            * for example: list("hey") --> ['h', 'e', 'y']
            * (split doesn't work with an empty separator)
        * for every character in the dictionary word...
            * if the character isn't in the temp list, that means that the
              dictionary word can't be formed by the letters in the temp 
              list... so stop, and don't add the word to your list of found
              words
            * if the character is in your temp list of characters, remove
              it from the temp list (so that it can't be "used" again)
            * once you've gone through all of the dictionary word's 
              characters, and they all existed (and have been removed) from 
              the temp list... you know the dictionary word can be formed by 
              the characters in your temp list! ...so add the word to your 
              list of found words
         * example:
            * set of letters: "tbe", current dictionary word: "be"
                * "b" from "be" is in ['t', 'b', 'e'] --> ['t', 'e']
                * "e" from "be" is in ['t', 'e'] --> ['t']
                * done... "be" can be formed from "tbe"
            * set of letters: "tbe", current dictionary word: "bee"
                * "b" from "bee" is in ['t', 'b', 'e'] --> ['t', 'e']
                * first "e" from "bee" is in ['t', 'e'] --> ['t', 'e']
                * second "e" from "bee" is NOT in ['t'] !!! 
                * done... "bee" CAN'T be formed from "tbe"

Example Interaction 1: max results are 3
-----
Please enter some letters... at least 1, but no more than 7
> tdri
What is the maximum number of words to display?
> 3
Showing max 3 results:
dirt
dit
id

Example Interaction 2: a non-numeric value is typed in, show all results
-----
Please enter some letters... at least 1, but no more than 7
> tdri
What is the maximum number of words to display?
> I don't want to say!
Showing all results:
dirt
dit
id
it
rid
ti

Example Interaction 3: keep on asking for letters if not all letters or 
number of letters not between 1 and 7 inclusive
-----
Please enter some letters... at least 1, but no more than 7
> 123
Please enter some letters... at least 1, but no more than 7
>
Please enter some letters... at least 1, but no more than 7
> abcdefghijklmnop
Please enter some letters... at least 1, but no more than 7
> tdri
What is the maximum number of words to display?
> 1
Showing max 1 results:
dirt
"""
