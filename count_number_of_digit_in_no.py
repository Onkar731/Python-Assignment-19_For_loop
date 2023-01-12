"""
Write a python script to count number of digits in a given number
"""

# taking input from the user
number = int(input("Enter a number : "))

# defining "count" to store count of digits
count = 0

# counting number of digits in a given number using for loop
# "int" is not an iterable that's why first convert "int" - "str"
# and access each element in string
for digit in str(number) :
    count += 1
    
# printing number of digits in a given number
print("Number of digits in a given number is : ", count)