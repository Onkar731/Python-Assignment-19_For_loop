"""
Write a python script to print each character of a string with its corresponding
unicode
"""

# printing each character of a string with its corresponding unicode using for loop
# taking string from the user
string = input("Enter a string : ")

for char in string :
    print(char, "->", ord(char))