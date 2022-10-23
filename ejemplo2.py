from machine import Pin 
import utime 

# declaracion de pines 

led_red = Pin(0,Pin.OUT) 
boton_green = Pin(26,Pin.IN)
 # Espacio de trabajo : 
led_red.value(0)
while True: 
    if boton_green.value()==1:
        led_red.value(1)
    else:
        led_red.value(0)



