#!/usr/bin/python3
from time import sleep
import pigpio

#setup pigpio object to work with
pi = pigpio.pi()

#make Pin 4 be an output pin, and turn off LED
pi.set_mode(4, pigpio.OUTPUT)
pi.write(4,1)

#Define/set variables
CYCLE_LENGTH_MIN = 7
BPM_START = 10
BPM_END = 5



sleep(2)

pi.set_PWM_range(4,100)

pi.set_PWM_dutycycle(4,100)
sleep(2)
pi.set_PWM_dutycycle(4,75)
sleep(2)
pi.set_PWM_dutycycle(4,50)
sleep(2)
pi.set_PWM_dutycycle(4,25)
sleep(2)
pi.set_PWM_dutycycle(4,0)

pi.stop()
