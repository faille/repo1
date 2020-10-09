from microbit import *
import radio

radio.config(channel=10)
radio.on()
number = 0
while True:
    display.show(str(number))
    incoming = radio.receive()
    if incoming == "+":
        number += 1
    elif incoming == "-":
        number -= 1
        if number < 0:
            number = 0
    if button_a.was_pressed():
        radio.send("+")
    if button_b.was_pressed():
        radio.send("-")
