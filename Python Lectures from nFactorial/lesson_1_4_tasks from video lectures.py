# Date: 07-08-2025

def mod (dividend, divider):    # Returns the remainder of dividing 'dividend' by 'divider' without using the % operator
    integer =( dividend // divider) # Integer part of division
    calculation_remainder = dividend - (divider * integer)  # Calculation of the remainder
    return calculation_remainder # Return the remainder
print(mod(14 , 17))




