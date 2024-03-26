


def calculator(num1, num2, operation):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
    elif operation == '*':
        result = num1 * num2
    
    return result

continue_or_end = True

num1 = float(input('Enter the first number: '))

while continue_or_end:

    
    operation = input('Enter the operation \n + \n - \n /\n *\n: ').lower()
    num2 = float(input('Enter the second number: '))
    
    result = calculator(num1, num2, operation)

    print(f"{num1} {operation} {num2} is {result} ")    

    continue_or_end = True if input("Do you want to continue(y or n)? ").lower()=='y' else False

    if continue_or_end:
        num1 = result