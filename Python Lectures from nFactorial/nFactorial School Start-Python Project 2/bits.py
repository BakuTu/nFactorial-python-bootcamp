# Date 2025-09-04

# Import required module
import sys  # Work with command line arguments

# Input validation
if len(sys.argv) < 2:   # Check if the number is provided
    print("Please provide a number as command argument")
    sys.exit()

# Convert argument to integer
n = int(sys.argv[1])

# Check negative input
if n < 0:
    print("Illegal input")
    sys.exit()

# Main calculation
count = 0   # Counter for divisions
while n >= 1:   # Keep dividing until number becomes < 1
    n = n / 2
    count += 1

# Output result
print(count)
