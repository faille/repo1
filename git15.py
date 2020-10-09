from microbit import *

def lumiere(row):
    for i in range(5):
        display.set_pixel(row, i, 9)

while True:
    intensity = display.read_light_level()
    #display.scroll(intensity)
    if intensity >= 0 and intensity <= 50:
        lumiere(0)
    if intensity > 50 and intensity <= 100:
        lumiere(1)
    if intensity > 100 and intensity <= 150:
        lumiere(2)
    if intensity > 150 and intensity <= 200:
        lumiere(3)
    if intensity > 200 and intensity <= 250:
        lumiere(4)
    sleep(1000)
    display.clear()
