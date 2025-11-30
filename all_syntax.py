eggs = 'global1'


def spam():
    global eggs
    eggs = 'spam'


spam()
print('Global value of eggs variable is = ', eggs)

list1 = ['dog', 'cat', 'horse']
list2 = list1  # both referencing to same list
list1.append("elephant")

list3 = list2[:]  # copying into a new list
list2.append("lion")

print("List1", list1)
print("List2", list2)
print("List3", list3)

print(list1+list2)  # + operator to concatenate lists
print(list1*3)      # * operator to repeat lists

del list1[0]  # deleting an element from list1
print(list2)  # list2 is also affected as both reference same list

for i in list2:
    print(i, end=' : ')
print()
# enumarating list elements with index tracking
for index, value in enumerate(list2):
    print(f"Index {index} has value {value}")

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

if 'Alice1' in names:
    print("Alice is in the list.")
elif 'Bob1' in names:
    print("Bob is in the list.")
else:
    print("Neither Alice1 nor Bob1 is in the list.")

a, b = 5, 10  # similar assignment work with lists as well
a, b = b, a  # swapping values
print("After swapping a =", a, " b =", b)

# index of an element in the list
print(f"Index of Bob in the names list is {names.index('Bob')}")

names.append('David')  # adding an element to the end of the list
names.insert(1, 'Eve')  # inserting an element at index 1
names.remove('Charlie')  # removing an element from the list
names.sort()  # sorting the list | can also use names.sort(reverse=True)

tpl = (1, 2, 3, 4, 5)  # tuple is IMMUTABLE unlike lists
tpl_to_list = list(tpl)  # converting tuple to list
list_to_tpl = tuple(names)  # converting list back to tuple

print(f"Tuple to List is now = {tpl_to_list}")
print(f"List to Tuple is now = {list_to_tpl}")

# Dictionary
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
for k in myCat:
    print(f"My cat's {k} is {myCat[k]}")

for k in myCat.keys():  # dictionary Keys
    print(f"My cat's {k} is {myCat[k]}")

for v in myCat.values():  # dictionary Values
    print(f"My cat has a {v}")

for k, v in myCat.items():  # dictionary Items with Keys & Values
    print(f"My cat's {k} is {v}")


if 'color' in myCat.keys():  # same for the values()
    print("Color key is present in the dictionary")

picnic_items = {'apples': 5, 'cups': 2}
# get() method with default value if key not found
print(f"I am bringing {picnic_items.get('cups', 0)} cups.")
# eggs key not present
print(f"I am bringing {picnic_items.get('eggs', 0)} eggs.")

# setdefault() method sets a key/value if not present
picnic_items.setdefault('eggs', 3)
print(f"Now I am bringing {picnic_items['eggs']} eggs.")

#  merging two dictionaries
x = {'a': 1, 'b': 2, 'c': 3}
y = {'b': 4, 'c': 5, 'd': 6}
z = {**x, **y}  # values from y will override those from x if keys are same
print(f"Merged dictionary z = {z}")

# Sets (un-ordered and No duplicate elements) , So you can't access elements with index
s1 = {1, 2, 3, 4, 5}
s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # another way to create set

s1.add(6)  # adding an element into set  , s1.remove(ele) OR s1.discard(ele) => discard don't show error if element not found
s1.update([5, 6, 7, 8, 9, 10])  # adding multiple elements at once

print(f"Set s1 is now {s1}")

# union of two sets, s1 | s2 also works See also, s1.intersection(s2) , s1.difference(s2)
# and s1.symmetric_difference(s2) => elements in either s1 or s2 but not in both
s3 = s1.union(s2)
print(f"Union of s1 and s2 is {s3}")

# List Comprehensions => doing st with each element of list in one line
numList = [1, 2, 3, 4, 5]
newNumList = [i - 1 for i in numList]  # subtracting 1 from each element
print(f"New Number List after subtracting 1 from each element = {newNumList}")

# Set Comprehensions
str_set = {'apple', 'banana', 'cherry'}
upper_set = {s.upper() for s in str_set}
print(f"Uppercase set = {upper_set}")

# Raw string => put a letter r in beggining of string to ignore escape sequences
print(r"C:\newfolder\testfile.txt")

# multiline string
multi_str = """This is a 
    multiline string example.
in python."""

print(multi_str)

# more string functions
"""
toupper() => upper case
tolower() => lower case
isupper() => check if all chars are upper case
islower() => check if all chars are lower case
strip() => remove leading and trailing whitespaces
replace(old, new) => replace old substring with new substring
find(substring) => returns starting index of substring or -1 if not found
startswith(substring) => checks if string starts with the substring
endswith(substring) => checks if string ends with the substring
str.split(separator) => splits string into list based on separator
str.strip() => removes leading and trailing whitespaces
str.rstrip() => removes trailing whitespaces
str.lstrip() => removes leading whitespaces
str.rjust(width, char) => right justifies string in given width
str.ljust(width, char) => left justifies string in given width
str.center(width, char) => centers string in given width
"""

join_list = ' - '.join(['apple', 'banana', 'cherry'])
print(f"Joined string from list = {join_list}")
my_name = ' WAQAS '
print(my_name.center(20, '*'))

# Raising your own exception based on an error code
# raise Exception("This is a custom exception message.")


# Assert
door_status = 'open'
# assert door_status == 'closed', "The door is not closed!"

# Power of lambda function


def make_adder(n):
    return lambda x: x + n


add_5 = make_adder(5)
add_10 = make_adder(10)
print(add_5(3))   # Outputs: 8
print(add_10(3))  # Outputs: 13

# *args and **kwargs


def fruits(*args, **kwargs):
    print("Fruits List:")
    for fruit in args:
        print(f"- {fruit}")
    print("Fruit Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


fruits('apple', 'banana', 'cherry', color='red', taste='sweet')
