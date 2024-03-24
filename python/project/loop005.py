# password generator
import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!','#','$','%','&','(',')','*','+']


no_of_length = int(input("How many letter: "))
no_of_symbols = int(input("How many symbols: "))
no_of_numbers = int(input("How many numbers: "))

password_list = []
for i in range(no_of_length):
    password_list.append(random.choice(letters))

for i in range(no_of_symbols):
    password_list.append(random.choice(numbers))

for i in range(no_of_numbers):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"The password is {password}")



"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""