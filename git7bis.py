from microbit import *

images = [Image.HAPPY, Image.SMILE,Image.SAD]
index = 0
display.show(images[index])
while True:
    if button_a.was_pressed():
        index += 1
        display.show(images[index%len(images)])
    elif button_b.was_pressed():
        index -= 1
        display.show(images[index%len(images)])
