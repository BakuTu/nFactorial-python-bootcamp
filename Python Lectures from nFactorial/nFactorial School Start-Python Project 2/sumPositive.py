
# Date 2025-08-16

# Block: Variable Initialization

# Create a variable to accumulate the sum of positive numbers, starting at 0
sum_positive_numbers = 0

# Before starting the main loop, we need to get the first valid integer from the user
# Keep asking until the user enters a correct integer
is_valid = False
while is_valid == False:
    print("Request new input")
    try:
        entered_number = int(input())
        is_valid = True
    except ValueError:
        # If input is not an integer, repeat the request
        is_valid = False

# 2 Block: Getting and Processing Data

# The loop will continue until the user enters a negative number
while entered_number >= 0:
    # If the entered number is positive, add it to the total sum
    if entered_number > 0:
        sum_positive_numbers += entered_number

    # After processing, request and validate the next input
    # Keep asking until the user enters a correct integer
    is_valid = False
    while is_valid == False:
        print("Request new input")
        try:
            entered_number = int(input())
            is_valid = True
        except ValueError:
            # If input is not an integer, repeat the request
            is_valid = False

    # 3 Block: Outputting the Result

    # When the user enters a negative number, stop the loop
    # Print the final sum of all positive numbers
    print(sum_positive_numbers)


