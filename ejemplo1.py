from machine import Pin 
import utime 

# declaracion de pines 

led_red = Pin(0,Pin.OUT) 

# Espacio de trabajo : 

while True: 

    led_red.value(1)
    utime.sleep_ms(500)
    led_red.value(0)
    utime.sleep_ms(500)



