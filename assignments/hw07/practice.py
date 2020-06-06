
def flattened(lst):
    """Given a list of lists, lst, create a new list composed of all
    elements from the sublists so that there are no longer any nested
    lists. 

    nested = [[1, 2], [3, 4]]
    flat = flattened(nested)
    print(flat) # --> [1, 2, 3, 4]

    :param lst: list of lists
    :type lst: list
    :return: flattened list
    :rtype: list
    """


def shift_left(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the left, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)  # no return value
    print(numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """


def shifted_left(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the left, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_left(numbers, 2)
    print(shifted_numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """


def shift_right(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the right, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)  # no return value
    print(numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """


def shifted_right(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the right, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_right(numbers, 2)
    print(shifted_numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """



def fill_in_place(lst, fill_value=0):
    """Fills an existing list, lst, with the value, fill_value.

    numbers = [1, 2, 3, 4]
    fill_in_place(numbers)
    print(numbers) # [0, 0, 0, 0]

    :param lst: the list to be filled with values
    :type lst: list
    :param fill_value: the value to fill the list with
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """


def truncate_long_words(words, n):
    """Creates a new list in which all words from the original list
    that have more than n characters are truncated so that only the
    first n characters followed by '...' are included in the new list

    print(truncate_long_words(['aardvark', 'bison', 'chameleon'], 5))
    # ['aardv...', 'chame...']

    YOU MUST USE A LIST COMPREHENSION TO DO THIS
    (no regular for loops or while loops allowed)


    :param words: list of words
    :type words: str
    :param n: any words less than or equal to n will not be included in new list
    :type n: int
    :return: new list only long words included... with each word truncated
    :rtype: list
    """


def sum_postive_pairs(lst):
    """Creates a new list that consists of the sum of each two-element
    tuple in the incoming lst... and only includes the sum if both
    elements in the tuple are positive.

    print(sum_postive_pairs([(1, 2), (3, 4)]))
    # [3, 7]

    YOU MUST USE A LIST COMPREHENSION TO DO THIS
    (no regular for loops or while loops allowed)

    Hint: you can unpack tuples in a list comprehension for clause to
    have two loop variables or you can use a built in function to 
    calculate the sum.

    :param lst: list of two element tuples
    :type list: list
    :return: new list of sums of every two-element tuple
    :rtype: list
    """


def consecutive_chars(start_ch, end_ch):
    """Creates a string consisting of all of the characters between
    start_ch and end_ch inclusive. If the start character appears
    after the end character, or if either the start character or
    end character are more than 1 character long, then an empty string
    is given back.

    print(consecutive_chars('A', 'Z'))
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(consecutive_chars('x', 'z')) # xyz
    print(consecutive_chars('Z', 'Z')) # ''
    print(consecutive_chars('Z', 'A')) # ''
    print(consecutive_chars('AAA', 'Z')) # ''

    YOU MUST USE A LIST COMPREHENSION TO DO THIS
    (no regular for loops or while loops allowed)

    Hint: the string method, join, and the built-in functions chr
    and ord may be helpful

    :param start_ch: list of words
    :type start_ch: str
    :param end_ch: list of words
    :type end_ch: str
    :return: a string consisting of all consecutive characters from start_ch
             to end_ch inclusive (or empty string)
    :rtype: str
    """

def unique(*lsts):
    """Creates a new set that consists of the unique elements of every list
    passed in. Notice that this takes in an arbitrary number of arguments.

    print(unique([1, 2, 3], [2, 3, 4], [3, 4, 5]))
    # {1, 2, 3, 4, 5}

    Hint: a new empty set can be created by using set() ... and set operators
    and methods typically give back a new set

    :param *lsts: a list of all lists passed in (all arguments collected as a 
                 list of lists)
    :type list: list
    :return: a set of unique elements across all lists
    :rtype: set
    """

if __name__ == '__main__':
    print("put your test cases here")
