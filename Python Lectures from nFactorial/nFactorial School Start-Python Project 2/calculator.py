# 2025-09-03

# Ask user to enter number
first_number = int(input())
second_number = int(input())

operation_to_perform = input("Enter operation to perform (+, -, *, /, %): ")

# Check operations
if operation_to_perform == "+":
    print(first_number + second_number)
elif operation_to_perform == "-":
    print(first_number - second_number)
elif operation_to_perform == "*":
    print(first_number * second_number)
elif operation_to_perform == "/":
    print(first_number / second_number)
elif operation_to_perform == "%":
    print(first_number % second_number)
else:
    print("Invalid operation")


