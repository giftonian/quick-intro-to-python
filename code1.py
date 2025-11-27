import copy
import pdb # for debugging
import time

def print_everything(*args):
   for count, thing in enumerate(args):
       print('{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')

def table_things(**kwargs):
   for name, value in kwargs.items():
       print('{0} = {1}'.format(name, value))

table_things(apple='fruit', cabbage='vegetable')

def myFun(arg1, arg2, arg3, arg4):
   print("arg1:", arg1)
   print("arg2:", arg2)
   print("arg3:", arg3)
   print("arg4:", arg4)

args = ("Geeks", "for", "Geeks", "PHIND")
myFun(*args)

kwargs = {"arg1":"Geeks", "arg2":"for", "arg3":"Geeks", "arg4":"Phind"}
myFun(**kwargs)

aLam = lambda x,y,z: x+y+z
print('a Lambda fun = ', aLam(1,2,3))

my_dict = {"name": "John", "age": 30, "city": "New York"}
for k in my_dict:
  print(my_dict[k])

list_comp = {x:7+1 for x in range(1, 10)}
for x in list_comp:
  print(list_comp[x])


# Shallow and Deep Copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list) # good

# Change in the shallow copy reflects in the original list
shallow_copy[0][0] = 100
print(original_list) # Outputs: [[100, 2, 3], [4, 5, 6]]


another_list = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(another_list) # costyly

# Change in the deep copy does not reflect in the original list
deep_copy[0][0] = 100
print(another_list) # Outputs: [[1, 2, 3], [4, 5, 6]]


# Decorators

def my_decorator(func):
   def wrapper():
       print("Something is happening before the function is called.")
       func()
       print("Something is happening after the function is called.")
   return wrapper

@my_decorator # equivalant to say_hello = my_decorator(say_hello)
def say_hello():
   print("Hello!")


say_hello()

def repeat(num_times):
   def decorator_repeat(f1):
       def wrapper():
           for _ in range(num_times):
               f1()
       return wrapper
   return decorator_repeat

@repeat(4)
def greet():
   print("Hello!")

greet()



def multiply(a, b):
   answer = a * b
   return answer

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# pdb.set_trace()
# result = multiply(x, y)
# print(result)

for i in range(1,10,2):
   print(i)

# Iterators in Python
"""
In Python, iterators are used to iterate a group of elements, containers like a list. Iterators are collections of
items, and they can be a list, tuples, or a dictionary. Python iterator implements __itr__ and the next() method to iterate the 
stored elements. We generally use loops to iterate over the collections (list, tuple) in Python.
"""


# Generators
'''
In Python, a generator is a special type of function that returns an iterator. An iterator is an object that contains a countable 
number of values and can be iterated upon, meaning that you can traverse through all the values.
Generators are created using functions and the yield statement. Instead of returning a value and terminating like a regular function, 
a generator yields a value and suspends its execution. The generator can then be resumed later on from where it left off, 
allowing it to produce a series of values over time, instead of computing them all at once and sending them back like a list
'''

def my_gen():
   n = 1
   print('This is printed first')
   yield n # save and return the value and wait for next call.

   n += 1
   print('This is printed second')
   yield n

   n += 1
   print('This is printed at last')
   yield n

a = my_gen()
print(next(a)) # 1
print(next(a)) # 2
print(next(a)) # 3 - This is the Max can be reached by Generator

for i in my_gen(): # loop through the Generator
   print('Generator value = ', i)

def upto_gen(n): # returns an Iterator
   if n < 0:
       return
   i = 0
   while i <= n:
       yield i
       i += 1
   print('Good by upto Generator!')

for i in upto_gen(10):
   print('Generating....', i)

class Book:
    def __init__(self, title, author, price):
        # Public member
        self.title = title
        
        # Protected member (by convention, use a single leading underscore)
        self._author = author
        
        # Private member (by convention, use two leading underscores)
        self.__price = price

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self._author)
        print("Price:", self.__price)

    # Public method
    def set_price(self, price):
        self.__price = price

# Creating an instance of the Book class
book_instance = Book("Python Programming", "John Doe", 29.99)

# Accessing public member
print("Title (public):", book_instance.title)

# Accessing protected member
print("Author (protected):", book_instance._author)

# Accessing private member (Note: It's still accessible, but not recommended)
# The name gets "mangled" to _Book__price
print("Price (private):", book_instance._Book__price)

# Using a public method to modify the private member
book_instance.set_price(39.99)

# Displaying information using a public method
book_instance.display_info()
