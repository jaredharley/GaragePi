#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

DEBUG = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
RED_LED = 25
GRN_LED = 24

GPIO.setup(GRN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def loop():
    GPIO.output(GRN_LED, GPIO.HIGH)
    GPIO.output(RED_LED, GPIO.LOW)
    time.sleep(1)
    GPIO.output(RED_LED, True)
    GPIO.output(GRN_LED, False)
    time.sleep(1)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit'
        while True:
            loop()
    finally:
        GPIO.cleanup()
