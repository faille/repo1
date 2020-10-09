from microbit import *

x = 0
y = 0
display.set_pixel(x, y, 9)
sleep(1000)
display.clear()
while True:
    for i in range(1, 5):
        display.set_pixel(i, y, 9)
        sleep(1000)
        display.clear()
        x = i
    for i in range(1, 5):
        display.set_pixel(x, i, 9)
        sleep(1000)
        display.clear()
        y = i
    for i in range(3, -1, -1):
        display.set_pixel(i, y, 9)
        sleep(1000)
        display.clear()
        x = i
    for i in range(3, -1, -1):
        display.set_pixel(x, i, 9)
        sleep(1000)
        display.clear()
        y = i
