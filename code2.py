# coding: utf-8
print("こんにちは世界")


def sprt():  # a simple console output separtor function
    print("----------------------------------------------------")


x = 5
y = 10
if x == y:
    print('x is eq to y')
elif x > y:
    print('x is gt y')
else:
    print('x is lt y')


sprt()
# loop
for i in range(10):
    print('iteration # ', i)

sprt()

for i in range(3, 27, 2):
    print('iteration from 3 to 27 with step=2 ', i)

print('Enter Table number to print')
# here type casting is necessary, otherwise it will be treated as String
table_num = int(input())

for i in range(1, 11, 1):
    print(table_num, " * ", i, " = ", table_num * i)

sprt()


def print_table(t_num):
    print('Welcome to printTable function')
    for i in range(1, 11, 1):
        print(f"{t_num}  *  {i}  =  {t_num * i}")  # f for formatter string


print_table(table_num)
sprt()

# unicode as an indentifier
وقاص = "Waqas Tariq Dar"
print(f"My name is {وقاص}")
sprt()

a = 10
b = 3
print(f"{a} raise to {b} is {a**b}")
print(f"Division of {a} and {b} is {a/b}")
print(f"Floor division of {a} and {b} is {a//b}")
sprt()

# Input => int(input("enter an integer")) OR float(input("enter a decimal value"))
income = float(input("Enter your monthly income: "))

if income < 50000:
    tax = income * 0.10
    print("Tax payable: ", tax)
elif 50000 <= income < 100000:
    tax = income * 0.20
    print("Tax payable: ", tax)
else:
    tax = income * 0.30
    print("Tax payable: ", tax)
