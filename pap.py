from machine import Pin
import time

pins= [
     Pin (19, Pin.OUT), # IN1
     Pin (18, Pin.OUT), # IN2
     Pin (17, Pin.OUT), # IN3
     Pin (16, Pin.OUT)  # IN4
     ]
secuencia = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
    ]

while True:
        for paso in secuencia:
            for i in range(len(pins)):
                pins[i].value(paso[i])
                time.sleep(0.02)
