from gpiozero import led
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
    #Green light
    green.on()
    red.off()
    yellow.off()
    sleep(4)

    #yellow light
    yellow.on()
    green.off()
    red.off()
    sleep(4)

    #red light
    red.on()
    yellow.off()
    green.off()
    sleep(4)