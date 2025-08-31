import turtle
import math
import time

# Создаем экран
screen = turtle.Screen()
screen.bgcolor("white")

# Создаем черепашку
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость
t.pensize(3)

# Настройки спирали
radius_start = 2  # Начальный радиус
radius_end = 30  # Конечный радиус
angle = 20  # Угол поворота
steps = 100  # Количество шагов
delay = 0.01  # Задержка

# Цвета для градиента
colors = ["red"]


# Функция для расчета координат спирали
def spiral_coordinates(r, angle):
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    return x, y


# Рисуем спираль
for i in range(steps):
    # Рассчитываем текущий радиус
    current_radius = radius_start + (radius_end - radius_start) * i / steps

    # Получаем координаты
    x, y = spiral_coordinates(current_radius, angle * i)

    # Перемещаемся в точку
    t.goto(x, y)

    # Меняем цвет
    t.pencolor(colors[i % len(colors)])

    # Добавляем задержку
    time.sleep(delay)

# Дополнительные настройки
t.hideturtle()
screen.mainloop()
