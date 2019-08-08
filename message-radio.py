from microbit import * 
import radio 
radio.on()
radio.config(channel=19) 
# Choose your own channel number
radio.config(power=7) 
# Turn the signal up to full strength 
my_message = "This is my message." 
# Event loop. 
while True: 
    radio.send(my_message) 
    incoming = radio.receive() 
    if incoming is not None: 
        display.show(incoming)
        print(incoming)
        sleep(500)