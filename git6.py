from microbit import *

chiffre = 0
x = 0
y = 0
while True:
    if button_b.was_pressed() and chiffre < 25:
        display.set_pixel(x, y, 9)
        chiffre += 1
        x += 1
        x = chiffre % 5
        y = chiffre // 5
    elif button_a.was_pressed() and chiffre > 0:
        chiffre -= 1
        x = chiffre % 5
        y = chiffre // 5
        display.set_pixel(x, y, 0)
