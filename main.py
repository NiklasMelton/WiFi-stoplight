from gpiozero import LED
from time import sleep

led_red = LED(12)
led_green = LED(19)
led_blue = LED(13)

while True:
    led_red.on()
    sleep(1)
    led_red.off()
    sleep(1)
    led_green.on()
    sleep(1)
    led_green.off()
    sleep(1)
    led_blue.on()
    sleep(1)
    led_blue.off()
    sleep(1)