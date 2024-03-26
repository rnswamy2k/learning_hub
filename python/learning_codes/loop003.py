# sum of even numbers from range of values.

total = 0
for i in range(1,101):
    if i%2==0:
        total+=i

print(f"Sum of all the even numbers between 1 to 101 is {total}")
