from microbit import *

x = 0
while True:
    if button_b.was_pressed() and x < 5:
        for y in range(5):
            display.set_pixel(x, y, 9)
        x += 1
    elif button_a.was_pressed() and x > 0:
        for y in range(5):
            display.set_pixel(x -1, y, 0)
        x -= 1
