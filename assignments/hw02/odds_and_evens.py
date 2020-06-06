"""
odds_and_evens.py
=====
Create a game of Odds and Evens where the player plays against the computer.

The rules of the game are here: 
https://en.wikipedia.org/wiki/Odds_and_evens

* Odds and Evens is played with two players
* one player is designated as odds and one player is evens
* both players agree to a play to a certain number of wins
* play proceeds as follows:
    * both player simultaneously show either 1 or 2 fingers
    * if the total of the fingers is odd, then the odds player wins
    * if the total of the fingers is even, then the evens player wins
    * the first player to meet the agreed upon number-of-wins wins the game

In our version of the game, start by:

* printing out:

    Let's play odds and evens

* ask the player if they want to be odds or evens
* if the player doesn't enter exactly odds or evens, then continue to ask:

    Do you want to be (odds) or (evens)?
    > NO. DO NOT WANT.
    Do you want to be (odds) or (evens)?
    > odds

* then... ask the player how many wins they want to set to win the entire game 
* and confirm that by displaying the number of wins required to win the game:

    What do you want to play up to?
    > 2
    Ok, 2 wins will win the entire game!

* if the number they put in is less than 1, do not play the game
* just print this message

    What do you want to play up to?
    > 0
    NO ONE WINS. GAME OVER!

* you do not have to handle a number of wins that is not numeric (you can
  assume that the user will, at least, put in a number!)
* if the number of wins is greater than 0, then proceed with the game

A "happy path" example of the beginning of the game may look like this:

    Let's play odds and evens
    Do you want to be (odds) or (evens)?
    > odds
    What do you want to play up to?
    > 3
    OK, 3 will win the entire game

Play will then proceed in rounds:

* the game continues round-by-round until either the computer or the player 
  exceeds the number of wins required to win the game
* print out the round number and the current score at the beginning of each
  round:

    Round 1
    =====
    Number of wins
    Player: 0, Computer: 0

* ask the player how many fingers they want to play, 1 or 2
* if the player does not enter a 1 or 2, proceed to the next round (skip
  everything else, including the computer's turn)
* you do not have to worry about non-numeric input (assume the player will
  enter a number)
* randomly generate the number of fingers for the computer - either 1 or 2
* display the number of fingers for both player and computer
* you can use the following emoji directly in your string:
    * http://emojipedia.org/white-up-pointing-index/
    * http://emojipedia.org/victory-hand/
* display whether or not the sum of the number of fingers played is odd
  or even
* display who won the round
* for example, in the case where player is odds and computer is evens:

    How many fingers will you play?
    > 1
    Player played ☝️️ (1)
    Computer played ☝️️ (1)
    Total is 2 (evens)
    Computer scores 1 win!

* once the computer or player reaches the number of wins specified in the
  beginning of the game, end the game, and display who won (player or 
  computer)

    Player wins the game!

* here's an example a full game:

    What do you want to play up to?
    > 3
    OK, 3 will win the entire game

    Round 1
    =====
    Number of wins
    Player: 0, Computer: 0

    How many fingers will you play?
    > 2
    Player played ✌️️ (2)
    Computer played ☝️️ (1)
    Total is 3 (odds)
    Player scores 1 win!

    OK, 3 will win the entire game

    Round 2
    =====
    Number of wins
    Player: 1, Computer: 0

    How many fingers will you play?
    > 1
    Player played ☝️️ (1)
    Computer played ✌️️ (2)
    Total is 3 (odds)
    Player scores 1 win!

    OK, 3 will win the entire game

    Round 3
    =====
    Number of wins
    Player: 2, Computer: 0

    How many fingers will you play?
    > 1
    Player played ☝️️ (1)
    Computer played ✌️️ (2)
    Total is 3 (odds)
    Player scores 1 win!

    Player wins the game!

"""
