# Date: 07-08-2025

current_number = 985    # Define the variable we will work with

last_digit = current_number % 10    # Get the last digit (units place)
first_digit = current_number // 100 # Get the first digit (hundreds place)
middle_digit = (current_number // 10) % 10  # Get the middle digit (tens place)

print(first_digit + middle_digit + last_digit)  # Print the sum of all digits