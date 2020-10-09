from microbit import *

sens_x = 1
sens_y = 0
x = 0
y = 0
while True:
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(500)
    x += sens_x
    y += sens_y
    if y == 0 and x < 4:
        sens_x = 1
        sens_y = 0
    if x == 4 and y < 4:
        sens_x = 0
        sens_y = 1
    if y == 4 and x > 0:
        sens_x = -1
        sens_y = 0
    if x == 0 and y > 0:
        sens_x = 0
        sens_y = -1
