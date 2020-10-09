from microbit import *
import radio

radio.config(channel=10)
radio_status = False
emission_status = False
while True:
    if button_a.was_pressed():
        radio_status = not radio_status
        if radio_status == True:
            radio.on()
            display.show(Image.YES)
        else:
            radio.off()
            display.show(Image.NO)
    if radio_status:
        if emission_status == False:
            incoming = radio.receive()
            if incoming:
                display.scroll(incoming)
                emission_status = True
        if emission_status:
            radio.send("OK")
