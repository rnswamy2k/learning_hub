from random import randint

LEVELS = {'hard':5, 'easy':10}

def validate_input(actuall, guessed):
    """
    This function validates the user input with actual
    """
    if actuall == guessed:
        return 0
    elif guessed>actuall:
        return 1
    else:
        return -1

while input("You want to play again(y or n): ").lower() == 'y':
    num = randint(1,100)
    level = input("Select the level (easy or hard)").lower()
    chances = LEVELS.get(level) or 0

    while chances>0:
        print(f"you have {chances}  chances left to complete!!!","\n")
        guess = int(input("Guess the number..! "))
        result =  validate_input(num, guess)
        chances-=1
        if chances == 0:
            print("You loose")
        elif result == 0:
            chances = 0
            print("You win!")
        elif result == 1:
            print("Its too high!")
        else:
            print("Its too low!")
        