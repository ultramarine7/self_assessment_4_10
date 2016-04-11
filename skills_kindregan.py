"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""
number_list = [1, 2, 7, -5]
odd_list = []

# Originally overthought this and was trying to write a code that reproduced a list. But assumed later
# the list is 1, 2, 7, -5.

# number_list = []
# i = 1
# while i < 3:
#     number_list.append(i)
#     i += 1

# i = -1
# while i > -3:
#     number_list.append(i)
#     i -= 1

def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    for num in number_list:
        if num % 2 != 0:
            odd_list.append(num)
    # print odd_list
    return []

number_list = [2, -6, 8]
odd_list = []

def all_odd(number_list):

    for num in number_list:
        if num % 2 == 0:
            odd_list.append(num)
    return []

all_odd(number_list)

##################################################################################

number_list = [2, 3, 5, 6, -1, -2]
even_list = []

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)
    return []

number_list = [-1, 3, 5]
even_list = []

def all_even(number_list):

    for num in number_list:
        if num % 2 != 0:
            even_list.append(num)
    # print even_list
    return []

all_even(number_list)

###################################################################

my_list = ["Toyota", "Jeep", "Volovo"]

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    for item, index in enumerate(my_list):
        print item, index

########################################################

word_list = ["all", "are", "tiny"]
long_word_list = []

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    word_length = 4

    for word in word_list:
        if len(word) > word_length:
            long_word_list.append(word)
    # print long_word_list
    return []

word_list = ["all", "are", "tiny"]
long_word_list = []

def long_words(word_list):

    word_length = 4

    for word in word_list:
        if len(word) > word_length:
            long_word_list.append(word)
    return []

#########################################################

number_list = [-5, 2, -5, 7]

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    for number in number_list:
        number = int(number)

        number_list.sort()
        minimum = number_list[0]
        small_list = minimum

        return small_list

number_list = [3, 7, 2, 8, 4]

def smallest_int(number_list):
    for number in number_list:
        number = int(number)

        number_list.sort()
        minimum = number_list[0]
        small_list = minimum

        return small_list

smallest_int(number_list)

########################################################

number_list = [-5, 2, -5, 7]

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    for num in number_list:
        num = int(num)

        number_list.sort()
        maximum = number_list[-1]

    return 

number_list = [3, 7, 2, 8, 4]

def largest_int(number_list):
    for num in number_list:
        num = int(num)

        number_list.sort()
        maximum = number_list[-1]

    return

largest_int(number_list)

##########################################################################

number_list = [2, 6, -2]
division_list = []

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    for num in number_list:
        division = float(num) / 2
        division_list.append(division)

    return

number_list = [1, 5]
division_list = []

def halvesies(number_list):
    for num in number_list:
        division = float(num) / 2
        division_list.append(division)

    return

halvesies(number_list)

###################################################################################

word_list = ["hello", "hey", "hello", "spam"]
length_list = []

def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    for word in word_list:
        length = len(word)
        length_list.append(length)

    return length_list

##############################################################################

sum_numbers = [1, 2, 3, 10]

def sum_numbers(number_list): # I had no idea there is sum() lol
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0
    for num in number_list:
        total = total + num
    return total

#############################################################################################

number_list = [1, 2, 3]

def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1
    for num in range(0, len(number_list)):
        total = total * number_list[num]
    return total

############################################################################################

word_list = ["spam", "spam", "bacon", "balloonicorn"]

def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    joined_list = ""
    for word in range(0, len(word_list)):
        joined_list = joined_list + word_list[word]
    return joined_list

join_strings(word_list)

###############################################################################

number_list = [2, 12, 3]

def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    average = 0
    sum = 0
    for num in number_list:
        sum = sum + num
        average = float(sum) / len(number_list)
    return average

average(number_list)

###########################################################################
list_of_words = ["Labrador", "Poodle", "French Bulldog"]

def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    for words in list_of_words:
        joined_words = ", ".join(list_of_words)
    return list_of_words

join_strings_with_comma(list_of_words)

##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
