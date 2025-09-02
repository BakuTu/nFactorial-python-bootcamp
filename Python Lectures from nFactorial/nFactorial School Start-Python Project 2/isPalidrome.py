# Date 2025-09-02
# Task: Check if input string is a palindrome

# Step 1. Ask user to enter a text
text = input("Please enter text: ")

# Step 2. Compare the text with its reversed version
if text == text[::-1]:
    # Step 3. Output result
    print(True)
else:
    print(False)