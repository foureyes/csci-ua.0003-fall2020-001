"""
pawesome_pet_vet.py 
=====
Write a program for managing the animals that are coming into a pet clinic. Use
the functions in animal_functions.py to help! Remember that the list of animals that are
checked in to the clinic is a list of lists. The outer list is the list of
animals, and each inner list reprsents a single animal:

* name will be at index 0
* type will be at index 1
* urgency will be at index 2

This is a cat named 'jane clawston' that does not have an urgent issue:

['jane clawston', 'cat', 10]

The list of all checked-in animals might look like this:

#       animal 1 --+        animal 2 --+        animal 3 --+
#                  |                   |                   |
var animals = [['zim', 'dog', 10], ['bev', 'dog', 10], ['ari', 'cat', 10]]

1. Your entire program should be contained within a single main function that
   does not have any parameters, and that does not return any values:
  
   def main()
       # do stuff
   
   main()

2. Within your main function, maintain a list of all checked-in animals
3. Initialize that list with the following animals:
   * a dog named edgrr allan pug, with an urgency of 80 
   * a cat named jane clawston, with an urgency of 20
   * a cat named franze catka, with an urgency of 60
   * a dog named bark twain, with an urgency of 40
4. Your pet clinic program will continually display a menu with possible 
   commands... until the user presses q to quit.
3. The menu looks like this:
   check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
   >
4. The following features should be supported:

check (i)n
=====
When a user checks in an animal (that is, they're coming into the pet clinic 
to be seen by the vet), they should be asked for:
1. the animal's name
2. the animal's type
3. the urgency of the animal's issue

If the number entered for urgency is not between 0 and 100 inclusive, 
continually ask the user for a number until they enter a valid value.

Once everything is valid, create a list representing the animal (just a list
literal... [val1, val2, val3]), and add it to your list of checked-in animals,
and print out a message saying that they're checked in - "{animal name} is
checked in"

Example Interaction for check (i)n:

    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > i
    What is the pet's name?
    > Jane Claweston
    What kind of animal is the pet?
    > Cat
    How urgently does the pet need help (0-100)?
    > 3000
    Please enter (0-100)
    > 100
    Jane Claweston is checked in!

check (o)ut
=====
When a user checks out an animal (that is, they're done with they're visit to
the clinic), they should be shown a list of all animals checked in, with a
number before each animal name and type.

The user should then be asked to enter the number of the animal to be checked
out. If the number is less than 1 or greater than the number of animals that
are checked in, print an error message and go back to the menu.

If the user enters a valid number, remove the animal from the list of checked
in animals, display the modified list, and print a message saying that 
{animal name} is checked out.

Example Interaction for check (o)ut:

    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > o
    1 - jane clawston, cat
    2 - franz catka, cat
    3 - bark twain, dog
    4 - edgrrr allan pug, dog
    Please enter a number to check an animal out of the clinic
    > 3
    1 - jane clawston, cat
    2 - franz catka, cat
    3 - edgrrr allan pug, dog
    bark twain is checked out
    
show (a)ll by name
=====
Show all by name displays all of the animals in the list of checked-in
animals in their original order.

Example Interaction for show (a)ll by name:

    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > a
    1 - bark twain, dog
    2 - edgrrr allan pug, dog
    3 - franz catka, cat
    4 - jane clawston, cat

(m)ost urgent and (l)east urgent
=====
Most urgent and least urgent will display the animal that has the most urgent 
and least urgent urgency value. The print out should be:

{animal name}, {animal type} with urgency {urgency of animal's issue}, should be seen right away!

or

{animal name}, {animal type} with urgency {urgency of animal's issue}, can wait!

Example Interaction for (m)ost urgent and (l)east urgent:

    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > m
    bark twain, dog with urgency 20, should be seen right away!
    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > l
    franz catka, cat with urgency 2, can wait!

(f)ind by name
=====
Find by name asks the user for a name, and then prints out the details of the
animal with that name (it's ok to just print the list)... or None if not found

Example Interaction:

    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > f
    Please enter a name to search for
    > jane clawston
    ['jane clawston', 'cat', 10]
    check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit
    > f
    Please enter a name to search for
    > bill furry
    None

"""
