# calculate the average height from the list. do not use len and sum functions

user_input = input("Enter the heights with comma separated : ")

heights = user_input.split(',')

total_height = 0
total_elements = 0
average_height = 0
if heights:
    for height in heights:
        total_height +=int(height)
        total_elements+=1


    average_height = total_height/total_elements

print(f"Average height of {heights} is {average_height} ")