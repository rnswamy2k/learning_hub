# https://en.wikipedia.org/wiki/Hangman_(game)
import random

words = ['chicago', 'seattle', 'columbus','dallas', 'austin']

word = list(random.choice(words))

# print(f'Select work is : {"".join(word)}')
result = list('_'*len(word))

loop = True
lives = 6
while loop:
    s = input('Choose a letter: ').lower()
    for k,v in enumerate(word):
        if v == s:
            result[k] = s 
    
    if s not in word:
        lives-=1

    print(result)
    if "_" not in result: 
        loop = False
        print("You win!")

    elif lives < 1:
        loop = False
        print("You loose!")

print(f" Here is the result - {''.join(result)}")