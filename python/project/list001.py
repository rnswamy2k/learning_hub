# Hide your treasure, given the row and column positions


list1 = [' ',' ',' ']
list2 = [' ',' ',' ']
list3 = [' ',' ',' ']

map = [list1, list2, list3]
letter = ['A','B','C']

user_input = str(input()).upper()

col_position = letter.index(user_input[0])

row_position = int(user_input[1])-1

map[row_position][col_position] = 'X'

for i in map:
    print(i)