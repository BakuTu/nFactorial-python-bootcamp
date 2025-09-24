# Date 2025-09-07

# Import necessary libraries
import turtle
import time
import random

# BLOCK 1: INITIALIZATION AND ENVIRONMENT SETUP

# Create a screen object on which the animation will be drawn
screen = turtle.Screen()

# Create a turtle object for drawing
t = turtle.Turtle()

# We set up the dimensions one width and height
screen.setup(width=400, height=330)

# Set the background color to black to simulate the night sky
screen.bgcolor("black")

# Hide the turtle icon so it doesn't interfere with the animation
t.hideturtle()

# We set the color mode to use RGB
screen.colormode(255)

# Set the turtle drawing speed to maximum (0)
# This makes the animation smoother and faster
t.speed(0)

# Disable automatic screen refresh\
# This allows us to control ech frame manually to create smooth animation
screen.tracer(0)

# Define the base colors for the stars in RGB
BASE_COLORS = [(255, 240, 170), (200, 200, 255)]

# We will store information about each star in a list of dictionaries
star_information = []
num_stars = 150 # Set the number of stars
for _ in range(num_stars):
    new_star = {
        # Random x and y coordinates within the screen boundaries
        "x": random.randint(-200, 200),
        "y": random.randint(-165, 165),
        # A andom base color for the star
        "base_color": random.choice(BASE_COLORS),
        # A random starting brightness (-150 to 0)
        "brightness" : random.randint(-150, 0),
        # A flag to control if the brightness is increasing or decreasing
        "increasing": random.choice([True, False])

    }
    star_information.append(new_star)

# Function to get the color based on brightness
def get_flickering_color(base_rgb, brightness):
    r = max(0, min(255, base_rgb[0] + brightness))
    g = max(0, min(255, base_rgb[1] + brightness))
    b = max(0, min(255, base_rgb[2] + brightness))
    return (r, g, b)

# The main animation function that will be called repeatedly
def animation_star():
    # Clear the previous frame
    t.clear()

    # Lift the "pen" so the turtle doesn't draw lines between stars
    t.penup()

    # Draw all the stars at their current positions
    for star in star_information:
        t.goto(star["x"], star["y"])
        # Get the current color of the star based on its brightness
        color = get_flickering_color(star["base_color"], star["brightness"])
        t.color(color)
        # Calculate the dot size so it pulsates
        # The size depends on brightness but remains small
        dot_size = max(2, (star["brightness"] + 150) / 30)
        t.dot(dot_size)

    # Update the brightness of each star for the next frame
    for star in star_information:
        if star["increasing"]:
            star["brightness"] += 2
            # If maximum brightness (0) is reached, start decreasing it
            if star["brightness"] >= 0:
                star["increasing"] = False
        else:
            star["brightness"] -= 2
            # If minimum brightness (-150) is reached, start increasing it
            if star["brightness"] <= - 150:
                star["increasing"] = True
    # Update the screen to show the new frame
    screen.update()

    # Star the animation by calling the function for the first time
    screen.ontimer(animation_star, 20)

# BLOCK 4: STARTING THE ANIMATION

# Start the animation by calling the function for the first time
screen.ontimer(animation_star, 0)

# Keep the window open until the user closes it
turtle.done()




