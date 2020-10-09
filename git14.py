from microbit import *
import radio

def clear_pixel_send(x, y):
    display.clear()
    display.set_pixel(x, y, 9)
    radio.send(str(x) + str(y))

radio.config(channel=10)
radio.on()
x = 2
y = 2
sensx = 1
sensy = -1
clear_pixel_send(x, y)
while True:
    incoming = radio.receive()
    if incoming:
        clear_pixel_send(x, y)
        display.set_pixel(int(incoming[:1]), int(incoming[1:]), 9)
    if button_a.was_pressed():
        x += sensx
        if x > 4:
            x = 3
            sensx = -1
        elif x < 0:
            sensx = 1
            x = 1
        clear_pixel_send(x, y)
    if button_b.was_pressed():
        y += sensy
        if y > 4:
            y = 3
            sensy = -1
        elif y < 0:
            sensy = 1
            y = 1
        clear_pixel_send(x, y)
