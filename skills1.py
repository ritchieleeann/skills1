# Things you should be able to do
some_list = [100, 20, 33, 4, 52, 60, 201, 20]
# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odds = []
    for items in some_list:
        if items % 2 == 1:
            odds.append(items)
    return odds
#print all_odd(some_list)
# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    evens = []
    for items in some_list:
        if items % 2 == 0:
            evens.append(items)
    return evens
#print all_even(some_list)

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
word_list = ["hi" , "hello" , "lol", "hola" , "conichiwa"]
def long_words(word_list):
    longs = []
    for items in word_list:
        if len(items) >= 4:
            longs.append(items)
    return longs
#print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    first = some_list[0]
    for items in some_list:
        if items < first:
            first = items
    return first
#print smallest(some_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    first = some_list[0]
    for items in some_list:
        if items > first:
            first = items
    return first
#print largest(some_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halves = []
    for items in some_list:
        halves.append(items/float(2))
    return halves
#print halvesies(some_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []
    for items in word_list:
        lengths.append(len(items))
    return lengths
#print word_lengths(word_list)

numbers = [8, 2, 22, 222, 208, 4]
# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    add = 0
    for items in numbers:
        add += items
    return add
#print sum_numbers(numbers)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult = 1
    for items in numbers:
        mult *= items
    return mult
#print mult_numbers(numbers)

string_list = ["hello" , "hi" , "hola"]
# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joint = ""
    for items in string_list:
        joint += items
    return joint
#print join_strings(string_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    add = 0
    av = len(numbers)
    for items in numbers:
        add += items
    return add / float(av)
print average(numbers)
