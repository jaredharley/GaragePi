#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RELAY_1 = 18
GRN_LED = 24
RED_LED = 25

GPIO.setup(RELAY_1, GPIO.OUT)
GPIO.setup(GRN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

GPIO.output(RED_LED, GPIO.HIGH)
GPIO.output(GRN_LED, GPIO.LOW)

def loop():
    GPIO.output(GRN_LED, GPIO.HIGH)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(RELAY_1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAY_1, GPIO.LOW)
    GPIO.output(GRN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(10)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit'
        while True:
            loop()
    finally:
        GPIO.cleanup()
