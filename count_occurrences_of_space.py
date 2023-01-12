"""
Write a python script to count occurrence of spaces in a given string
"""

# taking a string input from the user
string = input("Enter a string : ")

# defining count variable to count the occurrences of the space in a given string
count = 0

# counting occurrences of space in a given string using for loop
for char in string :
    if char == " " :
        count += 1

# printing occurrences of the space in a given string
print("Total count of space is", count)