from gpiozero import LED
from time import sleep
from subprocess import check_output
import http.client as httplib

led_red = LED(12)
led_green = LED(19)
led_blue = LED(13)

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
        led_blue.off()
        if internet_connected():
            led_red.off()
            led_green.on()
        else:
            led_green.off()
            led_red.on()
    else:
        led_green.off()
        led_red.off()
        led_blue.on()



if __name__ == '__main__':
    while True:
        print('red on')
        led_red.on()
        sleep(1)
        led_red.off()
        sleep(1)
        print('green on')
        led_green.on()
        sleep(1)
        led_green.off()
        sleep(1)
        print('blue on')
        led_blue.on()
        sleep(1)
        led_blue.off()
        sleep(1)