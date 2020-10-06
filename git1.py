from microbit import *
import radio

radio.on()

while True:
    incoming = radio.receive()
    if incoming:
        print(incoming)

    msg = uart.read()
    if msg:
        ch = msg[:2]
        ch = int(ch)

        radio.config(channel=ch)
        radio.send(msg[2:])
