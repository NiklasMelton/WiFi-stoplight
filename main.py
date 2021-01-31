from gpiozero import PWMLED, Button
from time import sleep
from subprocess import check_output
import http.client as httplib
import os

global WPS_SEARCH, IS_PULSING

button = Button(13,hold_time=1)
led_red = PWMLED(19)
led_green = PWMLED(12)
WPS_SEARCH = False
IS_PULSING = False
# led_blue = LED(13)

def wifi_up():
    wifi_ip = check_output(['hostname', '-I']).decode('UTF-8')
    open('/home/pi/hostname.log','a').write(str(wifi_ip))
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
    global WPS_SEARCH, IS_PULSING
    print('update leds',WPS_SEARCH)
    if wifi_up():
        IS_PULSING = False
        if internet_connected():
            led_red.value = 0
            led_green.value = 1
        else:
            led_green.value = 0
            led_red.value = 1
    elif not IS_PULSING:
        led_green.pulse()
        IS_PULSING = True

def WPS():
    global WPS_SEARCH
    print('WPS')
    led_red.off()
    led_green.off()
    IS_PULSING  =False

    WPS_SEARCH = True
    print('begin')
    os.system("/usr/sbin/wpa_cli -i wlan0 wps_pbc")
    led_green.pulse(fade_in_time=1, fade_out_time=1,n=60, background=False)
    # blink(120)
    # sleep(10)
    print('end')
    WPS_SEARCH = False

def blink(n=120):
    for i in range(n):
        led_red.on()
        sleep(0.5)
        led_red.off()
        sleep(0.5)




if __name__ == '__main__':
    button.when_held = WPS
    while True:
        if not WPS_SEARCH:
            update_LEDs()
        sleep(5)
        # print('red on')
        # led_red.value = 1
        # sleep(1)
        # led_red.value = 0
        # sleep(1)
        # print('green on')
        # led_green.value = 1
        # sleep(1)
        # led_green.value = 0
        # sleep(1)
        # print('yellow on')
        # led_green.value = 1
        # led_red.value = 0.5
        # sleep(1)
        # led_green.value = 0
        # led_red.value = 0
        # sleep(1)