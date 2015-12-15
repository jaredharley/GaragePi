#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define channels
RED_LED = 25
GRN_LED = 24
RELAY_1 = 16
DOOR_SENSOR = 18

# Set up channels
GPIO.setup(RELAY_1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(RED_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GRN_LED, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DOOR_SENSOR, GPIO.IN)

# Function to print channel status
def printChannelStatus(id, name):
    if GPIO.input(id):
        print('Channel ' + str(id) + ' (' + str(name) + ') is HIGH')
    else:
        print('Channel ' + str(id) + ' (' + str(name) + ') is LOW')

# Test inputs
printChannelStatus(16, 'RELAY_1')
printChannelStatus(18, 'DOOR_SENSOR')
printChannelStatus(24, 'GRN_LED')
printChannelStatus(25, 'RED_LED')
