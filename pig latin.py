"""Pig Latin Project"""
"""Take a word and return the pig latin version"""
""" Jesse Kniss """

# Take input from user
word = input("Enter a english word: ")

# Pull first letter from user input using slicing, change to lower case.
sLetter = word[:1].lower()

#If/else statements
if sLetter == "a" or sLetter == "e" or sLetter == "i" or sLetter == "o" or sLetter == "u":
    newWord = word + "way" 
else:
    newWord = word[1:] + sLetter + "ay"

print(word + " in pig latin is " + newWord)
