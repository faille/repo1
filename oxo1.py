from microbit import *
import radio

radio.on()
radio.config(channel=55)

while True:
    msg = uart.read()
    if msg:
        radio.send(msg)
    incoming = radio.receive()
    if incoming:
        x = int(incoming[:1])
        y = int(incoming[1:2])
        display.set_pixel(x, y, 9)
        if get_pixel(x-1, y) == 1 and get_pixel(x-2, y) == 9 or get_pixel(x+1, y) == 1 and get_pixel(x+2, y) == 9 or get_pixel(x, y-1) == 1 and get_pixel(x, y-2) == 9 or get_pixel(x, y+1) == 1 and get_pixel(x, y+2) == 9 or get_pixel(x-1, y-1) == 1 and get_pixel(x-2, y-2) == 9 or get_pixel(x-1, y+1) == 1 and get_pixel(x-2, y+2) == 9 or get_pixel(x+1, y-1) == 1 and get_pixel(x+2, y-2) == 9 or get_pixel(x+1, y+1) == 1 and get_pixel(x+2, y+2) == 9:
            game over
