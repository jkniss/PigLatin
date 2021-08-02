"""Pig Latin Project"""
"""Take a word and return the pig latin version"""
""" Jesse Kniss """

# Take input from user
word = input("Enter a english word: ")

# Pull first letter from user input using slicing, change to lower case.
sLetter = word[:1].lower()

#If/else statements
if sLetter == "a" or "e" or "i" or "o" or "u":
    newWord = word[1:] + sLetter + "ay"
else:
    newWord = word[1:] + "way"

print(word + " in pig latin is " + newWord)
