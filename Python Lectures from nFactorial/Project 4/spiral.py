# Date 2025-09-25
# Task 2: Hypnotic Spiral Animation

# Import necessary libraries
import turtle
import time
import random

# BLOCK 1: INITIALIZATION AND ENVIRONMENT SETUP

# Create a screen object
screen = turtle.Screen()

# Create a turtle object for drawing
t = turtle.Turtle()

# We set up the window dimensions
screen.setup(width=600, height=600)

# Set the background color to black
t.color("white")
screen.bgcolor("black")

# Hide the turtle icon
t.hideturtle()

# Set the turtle drawing speed to maximum
t.speed(0)

# Disable automatic screen refresh for smooth animation
screen.tracer(0)

# BLOCK 2: STATE VARIABLES

# Global variables that will change in every frame but will be RESET at the start of the function
step_length = 1
line_thickness = 0.5

# How much the entire spiral needs to be rotated in each frame to make it look spinning
global_angle = 0

# BLOCK 3: THE ANIMATION FUNCTION

def animate_spiral():
    # Declare global variables for modification
    global step_length, line_thickness, global_angle

    # *** ARCHITECTURAL FIX: Resetting spiral parameters for a new frame ***
    # This allows the spiral to start each frame from the center with minimal thickness
    step_length = 1
    line_thickness = 0.5

    t.clear()

    # ***ИСПРАВЛЕНИЕ: Поднимаем перо, чтобы не было следа от центральной линии***
    t.penup()
    t.goto(0, 0)
    t.setheading(global_angle) # Set the initial rotation heading
    t.pendown() # Опускаем перо, чтобы рисовать спираль

    # LOOP FOR DRAWING SPIRAL
    # ИЗМЕНЕНИЕ: Увеличили количество сегментов с 250 до 400, чтобы спираль была больше
    for i in range(400):
        t.pensize(line_thickness)
        t.forward(step_length)
        t.left(7)
        # Increment parameters
        # ИЗМЕНЕНИЕ: Увеличили шаг step_length с 0.02 до 0.05, чтобы увеличить расстояние между витками
        step_length += 0.05
        line_thickness += 0.02

    # ANIMATION AND RESET
    # 1. Increment the global angle so the next frame is rotated
    global_angle += 1

    # 2. Update the screen to show the new frame
    screen.update()

    # 3. Restart the function for the next frame (20 ms)
    # ИЗМЕНЕНИЕ: Уменьшили задержку с 20 мс до 10 мс для увелечения скорости
    screen.ontimer(animate_spiral, 10)

    # BLOCK 4: STARTING THE PROGRAM

# Start the animation immediately
screen.ontimer(animate_spiral, 0)

# Keep the window open and start the event loop (this is more reliable than 'turtle.done()' in some environments)
screen.mainloop()


