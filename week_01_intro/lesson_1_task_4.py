# Date 2025-08-13

# 1 Block: Get user input and validate

number_str = input("Please enter a five digit number: ")    # Ask for a five-digit number
# Check if input is digits and has length 5
if not number_str.isdigit():
    print("Please,enter only digits")  # Print error message
    exit()  # Stop the program
elif len(number_str) != 5:    # Check if the length is exactly 5
    print("Please, enter a five-digit number")  # Print error message
    exit()  # Stop the program
elif number_str[0] == '0':
    print("Number cannot start with zero")
    exit()

# 2 Block: Variable initialization

number = int(number_str)    # Convert string to integer
# Variables for counting even and odd digits
even = 0
odd = 0

# 3 Block: Loop to process digits
while number > 0:   # While there are digits
    last_digit = number % 10    # Get the last digit
    # Check if digit is even or odd
    if last_digit % 2 == 0:
        even += 1   # Increment even counter
    else:
        odd += 1    # Increment odd counter
    number = number // 10   # Remove the last digit

# 4 Block: Output the result

print(even, odd)    # Print counts of even and odd digits






