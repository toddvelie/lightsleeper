#!/usr/bin/python3
import time
import pigpio
from math import floor

#Declare constants
LED_PIN = 4
RAMP_LENGTH_MIN = 7
SETTLE_LENGTH_MIN = 5
START_BPM = 18.0
SLEEP_BPM = 15.0
BPM_DELTA_TOTAL = START_BPM - SLEEP_BPM
BPM_DELTA_PER_MIN = BPM_DELTA_TOTAL / RAMP_LENGTH_MIN

#Function: Take a breath
def Breath(pi, BPM):
    BREATH_LENGTH_SEC = 60.0 / BPM
    
    SLICE_TIME = BREATH_LENGTH_SEC / 200

    for i in range (100, 0, -1):
        pi.set_PWM_dutycycle(LED_PIN,i)
        time.sleep(SLICE_TIME) 

    for i in range (0, 100):
        pi.set_PWM_dutycycle(LED_PIN,i)
        time.sleep(SLICE_TIME) 

#Create a pigpio object to work with
pi = pigpio.pi()

#Make the GPIO pin an output, and turn off the LED
pi.set_mode(LED_PIN, pigpio.OUTPUT)
pi.write(LED_PIN, 1) 

#Drive LED using PWM
pi.set_PWM_range(LED_PIN,100)

try:

    END_TIME = time.perf_counter() + (60.0 * RAMP_LENGTH_MIN)
    while time.perf_counter() < END_TIME:
        CURR_MIN = (RAMP_LENGTH_MIN - 1) - floor(((END_TIME - time.perf_counter()))/60.0)
        CURR_BPM = START_BPM - (CURR_MIN * BPM_DELTA_PER_MIN)
        Breath(pi, CURR_BPM)

    END_TIME = time.perf_counter() + (60.0 * SETTLE_LENGTH_MIN)
    while time.perf_counter() < END_TIME:
        Breath(pi, SLEEP_BPM)    

finally:
    #Cleanup
    pi.write(LED_PIN, 1)
    pi.stop()
