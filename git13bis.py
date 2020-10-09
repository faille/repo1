from microbit import *

def sleep_clear(ret):
    sleep(1000)
    display.clear()
    return ret
x = 0
y = 0
display.set_pixel(x, y, 9)
sleep_clear(0)
while True:
    for i in range(1, 5):
        display.set_pixel(i, y, 9)
        x = sleep_clear(i)
    for i in range(1, 5):
        display.set_pixel(x, i, 9)
        y = sleep_clear(i)
    for i in range(3, -1, -1):
        display.set_pixel(i, y, 9)
        x = sleep_clear(i)
    for i in range(3, -1, -1):
        display.set_pixel(x, i, 9)
        y = sleep_clear(i)
