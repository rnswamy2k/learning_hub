# heightest value from the given list
user_input = input("Enter the heights with comma separated : ")

user_list = user_input.split(',')

value = 0 

if user_list:
    for num in user_list:
        if value<int(num):
            value = int(num)

print(f"Biggest number from {user_list} is {value}")