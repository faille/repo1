from microbit import *

value = 0
while True:
    for n in range(value):
        x = n % 5
        y = n // 5
        display.set_pixel(x, y, 9)
    if button_b.was_pressed() and value < 25:
        value += 1
    elif button_a.was_pressed() and value > 0:
        value -= 1
        display.clear()
