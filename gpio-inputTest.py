#!/usr/bin/env python
#coding: utf8 
import RPi.GPIO as GPIO
import webbrowser
import time
import os
from brotab.api import MultipleMediatorsAPI
from brotab.main import create_clients

api = MultipleMediatorsAPI(create_clients())
result = api.list_tabs([])
for line in result:
    print(line)

# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)
# Pin 18 (GPIO 24) als Eingang festlegen
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# Schleifenzähler
i = 0
# Endlosschleife
while 1:
    # Eingang lesen
    #print("test")
    if GPIO.input(18) == GPIO.LOW:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print("Eingang 18 HIGH" + str(i))
        # Schleifenzähler erhöhen
        i = i + 1
        time.sleep(1)

    if GPIO.input(16) == GPIO.LOW:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print("Eingang 16 HIGH" + str(i))
        # Schleifenzähler erhöhen
        i = i + 1
        time.sleep(1)

    if GPIO.input(13) == GPIO.LOW:
            # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
            print("Eingang 13 HIGH" + str(i))
            # Schleifenzähler erhöhen
            i = i + 1
            time.sleep(1)

    if GPIO.input(15) == GPIO.LOW:
            # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
            print("Eingang 15 HIGH" + str(i))
            # Schleifenzähler erhöhen
            i = i + 1
            time.sleep(1)
