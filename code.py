# Book => Python Interview Cheatsheet
print("Welcome to Python")
print(1/3) # decimal
print(1//3) # floor the answer

str_var = "I am String"
print(str_var)

#defining functions, Functions must be defined before(above) they are called in the script
def add(a, b):
    return a+b

def sprt(): # a simple console output separtor function
    print("----------------------------------------------------")

print("Addtion function called ", add(57.5, 43.7))

lst = [1, 2, 3, 4, 5] # this is a list
print(lst)
for i in lst:
    print('x by 2 = ', i*2, ' Square = ', i**2)

# input
#print('Enter your name.')
#myName = input()
#print('Hello, {}'.format(myName))

tp = ('1', '3', '5') # this is a tuple
print(tp)
for i in tp:
    print(i)

print('list length = ', len(lst))
print('tuple  length = ', len(tp))

# The ord() function in Python will return an integer that represents the Unicode char passed to it
# Print unicode of 'A'
print(ord('A'))
# Print unicode of '5'
print(ord('5'))
# Print unicode of '$'
print(ord('$'))

# implicit type casting
int_num = 100
float_num = 1.01
ans = int_num + float_num
print('int var + float var = ', ans)
print(type(int_num))
print(type(float_num))
# ans is implicitly typecasted to float type for greater precision
print(type(ans))

# explicit type casting
var = 123
var1 = str(var) # int to string
print(type(var1))
var = 123
# int to float
var1 = float(var) # int to float
print(var1)

var = 7.59
var1 = int(var) # float to int
print(var1) # Remember, original variable's type remains the same
print(var)
print(type(var1))
print("original float type = ", type(var))

# Relational operators
print(10 == 10)
print(10 <= 9)
flag = 5 <= 9
if (flag == True):  # or if(flag) is also enough
    print("5 is less eq to 9")

# Boolean operators, and, or, not
if (not 0):
    print("not operator testing")

if (5 == 5 and 7 > 4):
    print("and op testing")

if (5 == 5 or 7 > 4):
    print("or op testing")


# if/else structure
var = "Good"
if var == "Good":
    print("Var is capitalize Good")
    if 5 == 5:
        print("This is nested if")
elif var == "good":
    print("Var is small good")
else:
    print("Invalid Var, else case")

# Loops
for i in range(5): # default param of range(n) is stop, it means => 0 to 4 for range(5)
    print(i)

sprt()

for i in range(2, 10, 2): # start=2, stop=9, step=2
    print(i)

sprt()

a = [1, 3, 5, 7]
for ele in a: # for loop with "in" keyword
    print(ele)

sprt()

count = 5 
while count > 0: #while loop
    print(count)
    count -= 1
sprt()

# break statement
for i in range(5):
    print(i)
    if i == 3:
        break
sprt()

# continue statement
for i in range(5):    
    if i == 3: # skipping 3
        continue
    print(i)
sprt()

# pass: The pass statement is basically a null statement, which is generally used as
# a placeholder. It is used to prevent any code from executing in its scope.
# The pass statement is used as a placeholder for future code!!

for i in range(5):
    if i % 2 == 0:
        pass # do nothing
        print("help")
    else:
        print(i)
    print(i)

sprt()

# global statement
global value
value = "Global"
def fun1():
    global value # a global variable, just like PHP?
    value = "Local"

fun1()

print(value)
def fun2():
    global value
    value = "Updated val of global var"

fun2()
print(value)

sprt()

# modules
import math as mt
print(mt.pi)

# Exception handling, try, except, finally
# divide(4, 2) will return 2 and print Division Complete
# divide(4, 0) will print error and Division Complete
# Finally block will be executed in all cases
def divide(a, denominator):
    # your code will break without this try, except, block
    try:
        ans = a / denominator
        print(round(ans, 3))
        return ans
    except ZeroDivisionError as e:
        print('Divide By Zero!! Terminate!! ', e) # format(e)
    finally:
        print('Division Complete.')

divide(5, 0)
sprt()

# Lists -- values inside angle brackets []
days = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print(days)

print(days[0])
print(days[-1]) # Reverse accessing

print(days[0:2]) # +ve slicing, start:stop-1
print(days[2:4]) # +ve slicing, start:stop-1
print(days[-3:-1]) # -ve slicing, start:stop-1

rem_days = ["Thursday", "Friday"]
full_week = days + rem_days # concatenation lists
print(full_week)

rem_days = rem_days * 3  # Replicating lists
print(rem_days)

del full_week[1] # deleting a list elements

print(full_week)
for i in full_week:
    print(i)

print("Sunday" in full_week) # checking existence of an item in the list
flag = "Monday" not in full_week # checking non-existence
if flag:
    print("Monday not found in the list")

full_week.insert(1, "Monday") # Adding item at specified index
print(full_week)

full_week.append("Extraday") # Appending at the last of list
print(full_week)

full_week.sort() # Sorting a list
print(full_week)

full_week.sort(reverse = True) # Sorting a list in reverse order
print(full_week)
sprt()

# Tuples, immutable -- values inside small brackets
tpl = ("First", "Second", "Third", "Fourth")
print(tpl)
print(tpl[1:3])

# Type conversion between Tuples, Lists and Strings
# Convert list to a tuple
lst_to_tpl = tuple(['first', 'second', 'third'])
print(lst_to_tpl)
# Convert tuple to a list
tpl_to_lst = list(('first', 'second', 'third'))
print(tpl_to_lst)
# Convert string to a list
str_to_list = list("Scaler  is not a vector") # all characters will be separated, included spaces
print(str_to_list, ' : ', len(str_to_list))
word = ""
# count spaces and words in a string
for sp in str_to_list:
    if sp == " ":
        print("Space found")
        print(word)
        word = ""
    elif sp != " ":
        word += sp
print(word)
sprt()

# Python Dictionaries -- Key, value pairs inside curly braces {}
dict = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
# dict.keys() method will print only the keys of the dictionary
for key in dict.keys():
    print(key)
# dict.values() method will print only the values of the corressponding keys of the dic
for value in dict.values():
    print(value)

## updating/adding key value in dictionary
dict = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
for item in dict.items(): # .items() to access a complete item (Tuple) of Dictionary
    print(item)

dict['fourth'] = 'wednesday' # adding
dict['third'] = 'Fuesday'  # updating
for item in dict.items():
    print(item)

## deleting an item in dictionary
del dict['second']
print(dict)

## Merging two dictionaries
dict1 = {'first' : 'Waqas', 'second' : 'Tariq', 'third' : 'Dar'}
dict2 = {1: 3, 2: 4, 3: 5}
dict1.update(dict2)
print(dict1)
sprt()

# Sets -- distint values in curly braces {}
# A python set is basically an unordered collection of unique values, i.e. it will
# automatically remove duplicate values from the set.
s = {1, 2, 3}
print(s)
s = set([1, 2, 3])
print(s)
s = {1, 2, 3, 3, 2, 4, 5, 5} # duplication will be removed autometically
print(s)
s1 = {"my", "my", "name", 4, 5} # still, python will remove duplication
print(s1)

## Inserting elements in Sets
s.add(6)
print(s)

## Update elements in Sets
s.update([0, 7, 8, 9, 9, 10]) # pass a list of values
print(s)

## Delete elements from Sets
s.remove(4) # remove() will raise an error if the element is not in the Set
print(s)

s.discard(4) # discard doesn't raise any error if the element is not in the Set
print(s)

## operators used in Sets
a = {1, 2, 3, 3, 2, 4, 5, 5}
b = {4, 6, 7, 9, 3}
print(a & b) # Performs the Intersection of 2 sets and prints them
print(a | b) # Performs the Union of 2 sets and prints them
print(a - b) # Performs the Difference of 2 sets and prints them
print(a ^ b) # Performs the Symmetric Difference of 2 sets and prints them

sprt()

# Comprehensions
## List Comprehension: A shorter syntax to create a new list using values of an existing list.
a = [0, 1, 2, 3]
b = [i+1 for i in a] # +1 for each value of a and store in b
print(b)

## Set Comprehension: A shorter syntax to create a new set using values of an existing set.
s1 = {3, 5, 7, 9}
s2 = {i**2 for i in s1}
print(s2)

## Dict Comprehension: A shorter syntax to create a new dictionary using values of an existing dictionary.
a = {'Hello':'World', 'First': 1}
# b stores elements of a in value-key pair format
b = {val: k for k , val in a.items()}
print(b)
sprt()

# String Manipulation
## Multiline Strings,,,using triple quoutes
a = '''Hello
World!
This is a
Multiline String.'''
print(a)

str = "Computer Science"
print(str[3])  # String indexing is also 0-based
print(str[0:3]) # String slicing
print(str.upper())
print(str.lower()) # also check str.isupper(), str.islower(), isspace(), isalnum(), isalpha(), isTitle()

## join() and split() for Strings
list = ["One", "Two", "Three"]
# join function
s = ','.join(list)
print(s)

a = s.split(',')
print(a)

## String formating
first = "first"
second = "second"
s = "Sunday is the {} day of the week, whereas Monday is the {} day of the week".format(first, second)
print(s)
sprt()

# Formatting Dates
import datetime as dt
from datetime import datetime
tm = dt.time(1, 30, 11, 22)
print(tm)

date = dt.date(2000, 11, 16) # year, month, day
print('Date date is ', date.day, ' day of ', date.month, ' month of the year ', date.year)

## date to time
print(datetime.strptime('15/11/2000', '%d/%m/%Y'))
sprt()

# Regex
import re
landline = re.compile(r'\d\d\d\d-\d\d\d\d')
num = landline.search('LandLine Number is 2435-4153') # searching above regex format 4digits-4digits
print('Resultant number: {}'.format(num.group()))
## Grouping
landline = re.compile(r'(\d\d\d\d)-(\d\d\d\d)')
num = landline.search('LandLine Number is 2435-4153')
print(num.group(0)) # This will print the first group, which is the entire regex enclosed in the brackets
print(num.group(1)) # This will print the second group, which is the nested regex enclosed in the 1st set o
print(num.group(2)) # This will print the third group, which is the nested regex enclosed in the 2nd set of
## See page 45 of Python Interview Cheatsheet book for further Regex
sprt()

# Assert Statements -- when an assert fails, the program immediately crashes
sum = 4
# assert sum == 5, 'Addition Error'

print("Good going...")
sprt()

# Logging
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s')
logg = logging.getLogger() # Creates logging object
logg.setLevel(logging.DEBUG) # Sets the level of logging to DEBUG
# Messages
logg.debug("Debug Message")
logg.warning("Its a Warning")
logg.info("Just an information")
sprt()

# Lambda Function in Python
# These are small anonymous functions in python, which can take any number of
# arguments but returns only 1 expression.

def mul(a, b):
    return a * b
print(mul(3, 5))

mult = lambda a,b,c : a * b * c
print(mult(2, 3, 5))
sprt()

# Ternary Operator
f = 2
s = 2
# if the sum of f and s is greater than 0 the sum
# is printed, else 0 is printed
print(f + s if (f + s > 0) else 0)
sprt()

# *args and **kwargs in Python
## *args: For non-keyword arguments.
def tester(*argv):
    for arg in argv:
        print(arg)
tester('Sunday', 'Monday', 'Tuesday', 'Wednesday')

## **kwargs: For keyword arguments.
# The function will take variable number of arguments
# and print them as key value pairs
def tester(**kwargs):
    for key, value in kwargs.items():
        print('key = ', key, ', value = ', value)
tester(Sunday = 1, Monday = 2, Tuesday = 3, Wednesday = 4)
sprt()

print("Good bye Python first class!")
