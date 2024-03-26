# encryption & decryption
from string import ascii_lowercase, ascii_uppercase, printable

continue_or_end = True


# letters = list(printable.replace(ascii_uppercase, ' '))

letters = list(ascii_lowercase)
letter_len = len(letters)

def caesar(direction,txt, shift):

    result = list('_'*len(txt))

    if shift<0:
        shift*=-1

    if shift>26:
        shift %=26

    for k,v in enumerate(txt):
        if v not in letters:
           result[k] = v
        else:
            pos = letters.index(v)
            if direction=='e':
                new_pos = pos + shift
            else:
                new_pos = pos - shift

            if new_pos > 25:
                new_pos = new_pos - 26
            elif new_pos < 0:
                new_pos=26+new_pos        
            result[k] = letters[new_pos]
    return ''.join(result)


while continue_or_end:

    task = input("Encrypt(e) or decrypt(d)").lower()
    txt = input("Enter the string to encrypt: ").lower()
    shift = int(input("Enter the shift number: "))

    print(caesar(task, txt, shift))
    
    continue_or_end = True if input("Do you want to continue(y or n)? ").lower()=='y' else False

