# Date 2025-08-20

# Block 1: Variable Initialization

# Create a variable to store the correct password
password = "Nfac129_"

# Create a variable to store the number of attempts
number_of_attempts = 3


# Block 2: Loop and password check

# The loop will run exactly 3 times
for i in range(number_of_attempts):

    # Get input from the user
    entered_password = input("Enter a password: ")

# Check if the password matches
    if entered_password == password:
    # If it matches, print the correct password message and exit the loop
        print("Correct password!")
        break
    else:
        # If it doesn't match, calculate and print the number of remaining attempts
        remaining_attempts = number_of_attempts - (i + 1)
        print(f"Incorrect password. You have {remaining_attempts} attempts left.")


    # Block 3: Final Output

    # This 'else' block executes only if the loop finishes without a 'break'
else:
    # Print the blocking message because all attempts have been exhausted
    print("You have entered the password incorrectly 3 times. Account blocked.")





