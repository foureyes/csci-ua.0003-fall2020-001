"""
animal_functions.py - 12 points
=====
Write four functions that work with nested lists:

1. find_by_name(name, animals)
2. stringify_animals(animals)
3. get_most_urgent(animals)
4. sort_by_name

The parameter, animals, will be a list of lists representing a collection 
of animals at veterinary clinic (animal hospital!). The outer list is all 
of the animals, while each inner list is a single animal with:

* a name ('jane clawston')
* a type / kind ('cat')
* a number representing urgency - 0-100, with 100 the most urgent and 0 as
not urgent at all)

The attributes listed above for a single animal is represented by a 3 
element list:

* name will be at index 0
* type will be at index 1
* urgency will be at index 2

For example, a cat named 'jane clawston' that does not have an urgent issue
can be represented as:

['jane clawston', 'cat', 10]

So... a list of animals will look like: 

#             animal 1 ------+            animal 2 ------+ 
#                            |                           |
animals = [['jane clawston', 'cat', 10], ['franz catka', 'cat', 2]] 

Write the following functions that have a list of animals as a parameter.

find_by_name:
-----
Returns the animal with the name specified from a list of animals. 

* parameters: 2 - a string (the name to search for), and a list of animals
* processing:
    1. go through every animal in the list
    2. checks the name
    3. if the name matches the supplied name, give back that animal
* return value: a single animal (a list) or None if the animal is not found

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
res = find_by_name('sam', animal_list) 
print(res) # ['sam', 'snake', 4]


stringify_animals:
-----
Create a string representing the list of animals using their name, kind, 
and the position they're in within the list (using 1 as the first animal, 
rather than 0).

* parameters: a list of animals
* processing:
    1. go through every animal in the list
    2. accumulate each animal's position, name and type
* return value: the resulting string formatted as:

1 - sam, snake
2 - gertrude, goat
3 - ang, unicorn

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]

# returns the string: "1 - sam, snake\n2 - gertrude, goat\n3 - ang, unicorn"
res = stringify_animals(animal_list)

print(res)

1 - sam, snake
2 - gertrude, goat
3 - ang, unicorn


get_most_urgent:
-----
This function will find the animal that has the most urgent issue in a list of animals.

* parameters: a list of animals (a list of lists)
* processing:
    1. iterates through entire list of animals
    2. checks the urgency value of each animal
    3. finds the animal with the highest urgency value
    4. if urgency values are the same, choose any animal (it's easiet to
       just choose the last one with the highest value)
* return value: a single animal (a list)

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(get_most_urgent(animal_list))
# will print out ['gertrude', 'goat', 99]


sort_by_name:
-----
This function will return a new list of animals, sorted by the name of the 
the animal (that is, the first element in the list that represents a single 
animal), based on the original list of animals given to the function. The
result will be a new list of animals sorted alphabetically by name.

* parameters: a list of animals (a list of lists)
* processing:
    1. DO NOT USE THE LIST'S SORT METHOD, instead, follow this process
    2. go through every animal in the list positionally (that is, look at the
       first animal, the second, third, etc...)
    3. compare the name of the current animal with the name of the next animal
    4. if the name of the current animal goes after the name of th next animal,
       swap animals
    5. remember, the idiomatic way of swapping in python is a, b = b, a (but
       be careful, as you'll have to swap two elements in a list!)
    6. of course, once you're at the last element, there's no next element to 
       check
    7. once you've gone through all of the animals... REPEAT the whole process
       if you've swapped at least once
    8. stop repeating the process when no swaps occur after going through the
       entire list
    9. here's an example of how it might work:
       element 1: swap with next
       [['zim', 'dog', 10], ['bev', 'dog', 10], ['ari', 'cat', 10]]
       element 2: swap with next
       [['bev', 'dog', 10], ['zim', 'dog', 10], ['ari', 'cat', 10]]
       element 3: last element, do not compare!
       [['bev', 'dog', 10], ['ari', 'cat', 10], ['zim', 'dog', 10]]

       element 1: swap with next
       [['bev', 'dog', 10], ['ari', 'cat', 10], ['zim', 'dog', 10]]
       element 2: do not swap!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]
       element 3: last element, do not compare!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]

       element 1: do not swap!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]
       element 2: do not swap!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]
       element 3: last element, do not compare!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]

       No swaps occurred... so stop repeating process.

* return value: a list of animals, alphabetically sorted by name

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
sorted_animal_list = sort_by_name(animal_list)
print(sorted_animal_list)
# will print out [['ang', 'unicorn', 50], ['gertrude', 'goat', 99], ['sam', 'snake', 4]]
"""
