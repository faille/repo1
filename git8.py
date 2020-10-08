from microbit import *
import radio

radio.config(channel=10)
radio.on()
images = [Image.HAPPY,Image.SMILE,Image.SAD]
index = 0
display.show(images[index])
while True:
    incoming = radio.receive()
    if incoming:
        display.show(images[int(incoming)])
    else:
        if button_a.was_pressed():
            index += 1
            display.show(images[index%len(images)])
        elif button_b.was_pressed():
            index -= 1
            display.show(images[index%len(images)])
        elif accelerometer.was_gesture("shake"):
            radio.send(str(index))
