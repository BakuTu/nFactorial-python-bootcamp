# Date: 08-08-2025

vowel_set = frozenset({'a', 'e', 'i', 'o', 'u', 'y'})   # Set of vowel letters that cannot be changed after creation

def check_character(character): # Check conditions of character
    if character.isalpha(): # Checks if the character is a letter
        if character.lower() in vowel_set:  # Check if the character (lowercased) is a vowel
            print("User input: Vowel")
        else:
            print("User input: Consonant")
    elif character.isdigit():   # Checks if the character is a digit
        print("User input: Digit")
    else:
        print("User input: Symbol") # Run if answer is not in previous answers

check_character('a')
check_character('b')
check_character('7')
check_character('@')










