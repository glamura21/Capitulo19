from machine import Pin
import time

boton=machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

pins= [
     Pin (19, Pin.OUT), # IN1
     Pin (18, Pin.OUT), # IN2
     Pin (17, Pin.OUT), # IN3
     Pin (16, Pin.OUT)  # IN4
     ]
secuencia = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]
secuencia2 = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
    ]

while True:
    if boton.value() == 0:
        for paso in secuencia:
            for i in range(len(pins)):
                pins[i].value(paso[i])
                time.sleep(0.002)
    elif boton.value() == 1 :
        for paso in secuencia2:
            for i in range(len(pins)):
                pins[i].value(paso[i])
                time.sleep(0.002)
