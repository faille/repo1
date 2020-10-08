from microbit import *

direction = 0
display.show(Image.ALL_CLOCKS[direction%12])
while True:
    if button_a.was_pressed():
        direction += 1
        display.show(Image.ALL_CLOCKS[direction%12])
    elif button_b.was_pressed():
        direction -= 1
        display.show(Image.ALL_CLOCKS[direction%12])
