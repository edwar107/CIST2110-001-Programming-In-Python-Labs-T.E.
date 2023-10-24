# Lab6
# Author: Terrisha 

# Write a function that calculates the area of a rectangle given its width and height 

def calculate_rectangle_area(width:float , height:float)
    return width * height
    ***_Calcuate the area of a rectangle given its width and height

    Args:
    side_a (float): Length of side A
    side_b (float): Length of side B

    Returns: 
    float: Length of the hypotenuse

    sides = side_a**2 + side_b**2
    from math import sqrt
    return math.sqrt(sides) 
    
    return width * height

def calcuate_hypotenuse(side_a: float, side_b: float)
    #calcuate_hypotenuse will calcuate the hypotenuse of a right triangle given the lengths of the other two sides.
    #Pythagorean theorem: a^2 + b^2 = c^2

    return (side_a**2 + side_b**2)**0.5

##Write a functin that determines if a number is even. 

def is_even(number: int) ==>bool: 

    Args: 
    number (int): Number to check

    Returns:
    bool: True if number is even, False otherwise

    if number % 2 = 0
        return True 
    else:
        return False
    
def find_maximum(number1: float, number2: float)
    #Determine the maximum of two numbers.

    Args:
    number1 (float): First number
    number2 (float): Second number

    Returns:
        float: The maximum of the two numbers
    
    if number1 > number2:
        return number1
    else:
        return number2
    
##Write a function that calculates a letter grade for a given score.

     ##Calcuate a letter grade for a given score.

    Args:
    score (float):"Score to calcuate"
     
Returns: 
    str: "Letter grade"


if score > 90 and score < 100:
    return "A"
elif score > 80 and score < 90:
    return "B"
elif "score" > 70 and "score" < 80:
    return "C"
elif "score" > 60 and "score" < 70:
    return "D"
elif "score" > 0 and "score" < 60:
    return "F"
else:
    return "Invalid score" 












## add in functions from test.py's test statements here to make the pytest work

def main(): 
    pass


if __name__ == "__main__":
    main()
