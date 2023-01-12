"""
Write a python script to print unique digits of a given integer
"""

# taking input from the user
num = int(input("Enter a number : "))

# defining empty string variable
string = str()

# printing unique digits of a given integer
for digit in str(num) :
    if digit not in string :
        print(digit, end= ' ')
        string += digit
