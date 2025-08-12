# Date: 2025-08-10
# Compare Three Numbers

# Goal: Sort three numbers and print them separated by a space

# 1. Data Collection
# We save the entered numbers in variables for further processing

order_1 = int(input("First number: "))
order_2 = int(input("Second number: "))
order_3 = int(input("Third number: "))

# 2. Data Processing
# We create a list, sort it, and prepare an empty list for strings
numbers_list = [order_1, order_2, order_3]
numbers_list.sort()

string_list = []

# 3. Data Transformation
# A loop that converts each number to a string and adds it to a new list
for number in numbers_list:
    string_list.append(str(number))

# 4. Output Result
# Join the list of strings into a single string to the screen
print(' '.join(string_list))
