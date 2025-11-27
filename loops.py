from helpers import sprt
# Print even numbers on single line with for loop
for i in range(2, 101, 2):
    print(f'{i}', end=' ')

sprt()

# For loops in List
food_items = ['Milk', 'Eggs', 'Apples']
for food in food_items:
    print(food)


# While loop
counter = 1
while counter <= 10:
    print(f'Counter = ', {counter})
    counter += 1

prompt = 'Enter a number or type quit to exit: '
while True:
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        print('Good bye!')
        break
    else:
        print(f'You entered : {user_input}')

# While loop to print 1 to 10 table

while True:
    try:
        num = int(input('Enter table number to print table: '))
    except ValueError:
        continue

    for i in range(1, 11):
        print(f'{num} * {i} = {num*i}')

    choice = input('Do you want to conitnue? y/n: ').strip().lower()
    if choice == 'n':
        break
    else:
        print("Let's print another table")
