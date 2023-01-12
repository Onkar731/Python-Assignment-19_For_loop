"""
Write a python script to print only vowels of the given string
"""

# taking a string input from the user
string = input("Enter a string : ")

# printing vowels of the given string using for loop
for char in string :
    if char in "aeiouAEIOU" :
        print(char, end=' ')