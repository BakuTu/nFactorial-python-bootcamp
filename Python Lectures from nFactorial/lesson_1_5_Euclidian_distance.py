# Date: 07-08-2025
# Euclidian Distance

def euclidean_distance(x1, y1, x2, y2): # This function takes the coordinates of two points and returns the distance between them using the Euclidean distance formula
    total_distance = ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5  # Calculate the total distance using the Pythagorean theorem
    return total_distance   # Return total distance
print(euclidean_distance(0, 0, 3, 4))
