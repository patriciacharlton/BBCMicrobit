from microbit import * 
while True:
    temp = temperature()
    display.scroll(str(temp) + 'C')
    sleep(500)