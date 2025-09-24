import turtle

def draw_fractal(x, y, r, n, color1, color2):
    turtle.up()
    turtle.goto(x, y -r)
    turtle.down()
    turtle.fillcolor(color1 if n % 2 == 0 else color2)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

    if n > 1:
        draw_fractal(x - r/2, y, r/2, n-1, color1, color2)
        draw_fractal(x + r/2, y, r/2, n-1, color1, color2)

screen = turtle.Screen()
screen.tracer(0)

turtle.speed(0)
turtle.hideturtle()

draw_fractal(0, 0, 120, 4, 'cyan', 'magenta')

screen.update()
turtle.done()