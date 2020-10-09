from microbit import *

while True:
    intensity = display.read_light_level()
    #display.scroll(intensity)
    display.clear()
    if intensity > 249:
        intensity = 249
    for x in range(intensity /// 50 + 1):
        for y in range(5):
            display.set_pixel(x, y, 9)
