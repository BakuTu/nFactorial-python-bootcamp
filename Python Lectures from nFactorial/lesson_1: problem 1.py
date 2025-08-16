# Date: 2025-08-05
# 1. Check if a Character is a Vowel or Consonant
# Write a program that takes a single character as input if it is a vowel, constant, or not a letter.
# For this problem only 'aeiou' are considered to be vowels.

import string
vowels = 'aeiou'
all_letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyz'
consonants = ''.join([ch for ch in all_letters if not ch in vowels])
letter = input()
if letter.isalpha():
    print("This is a letter")
elif letter.lower() in vowels:
    print("This is a vowels letter")
elif letter.lower() in consonants:
    print("This is a consonants letter")
elif letter.isdigit():
    print("This is a digit")
else:
    print("This is a special character")

