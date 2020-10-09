from microbit import *

x = 0
sens = 1
while True:
    display.clear()
    display.set_pixel(x, x, 9)
    x += sens
    if x > 4:
        x = 3
        sens = -1
    elif x < 0:
        sens = 1
        x = 1
    sleep(1000)
