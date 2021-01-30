from gpiozero import PWMLED
from time import sleep
from subprocess import check_output
import http.client as httplib

led_red = PWMLED(19)
led_green = PWMLED(12)
# led_blue = LED(13)

def wifi_up():
    wifi_ip = check_output(['hostname', '-I'])
    return wifi_ip is not None

def internet_connected():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def update_LEDs():
    if wifi_up():
        if internet_connected():
            led_red.value = 0
            led_green.value = 1
        else:
            led_green.value = 0
            led_red.value = 1
    else:
        led_green.on()
        led_red.on()



if __name__ == '__main__':
    while True:
        print('red on')
        led_red.value = 1
        sleep(1)
        led_red.value = 0
        sleep(1)
        print('green on')
        led_green.value = 1
        sleep(1)
        led_green.value = 0
        sleep(1)
        print('yellow on')
        led_green.value = 1
        led_red.value = 0.5
        sleep(1)
        led_green.value = 0
        led_red.value = 0
        sleep(1)