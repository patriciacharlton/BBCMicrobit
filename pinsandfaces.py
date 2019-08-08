from microbit import *
 
while True:
    # if button_a.is_pressed():
    #if pin0.read_digital():
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)