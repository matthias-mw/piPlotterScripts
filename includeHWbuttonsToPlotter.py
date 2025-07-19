#!/usr/bin/env python
#coding: utf8 
import RPi.GPIO as GPIO
import webbrowser
import time
import os
from brotab.api import MultipleMediatorsAPI
from brotab.main import create_clients
import subprocess

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Config Data
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Activate the Anchor Watch Tab
urlButton1 = "http://tatooinepi:3333/d/ednkv6r5ez0n4c/anchor-watch?orgId=1&var-myTime=3h&from=now-1h&to=now&timezone=browser&refresh=1m"
tabButton1 = "Anchor Watch"

# Activate the SV Tattoine Remote Tab
urlButton2 = "http://tatooinepi:3333/d/-gsoO687z/sv-tatooine-remote?orgId=1&from=now-7d&to=now&timezone=Europe%2FBerlin"
tabButton2 = "SV Tatooine Remote"

# Activate the SV Tattoine Remote Tab
urlButton3 = "http://tatooinepi:3333/d/-gsoO687z/sv-tatooine-remote?orgId=1&from=now-7d&to=now&timezone=Europe%2FBerlin"
tabButton3 = "SV Tatooine Remote"

# Activate OpenCPN
wndOCPNtitle = "OCPN"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Function to focus on a given window and bring it in front
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def focus_window_by_title(title_keyword):
    try:
        # List all windows
        output = subprocess.check_output(['wmctrl', '-l']).decode('utf-8')

        # Search for the window by title keyword
        for line in output.splitlines():
            if title_keyword.lower() in line.lower():
                window_id = line.split()[0]
                subprocess.run(['wmctrl', '-ia', window_id])
                print(f"Brought window to front: {line}")
                return

        print(f"No window found with title containing: '{title_keyword}'")

    except Exception as e:
        print(f"Error: {e}")



# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)
# Pin 18 (GPIO 24) als Eingang festlegen
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Active a certain Webbrowser Tab
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def select_tab(tab_title,url):
    
    api = MultipleMediatorsAPI(create_clients())
    result = api.list_tabs([])

    tabCnt = 0
    for line in result:
        print(line)

        # Check for "tab_title" and extract the string before the first space
        if tab_title in line:
            tabID = line.split()[0]
            tabCnt = tabCnt + 1
            print(tab_title + " found.")
            # Close if multible tabs were found
            if tabCnt > 1:
                result = api.close_tabs([tabID])
                print("One Tab closed")
            else:
                result = api.activate_tab([tabID],True)

    #If ther is no Open Anchow Watch tab
    if tabCnt == 0:
        webbrowser.open_new_tab(url)

    focus_window_by_title(tab_title)

# Endlosschleife
while 1:
    
    # --- Button1 ---
    if GPIO.input(15) == GPIO.LOW:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print("Eingang 15 HIGH" )
        
        select_tab(tabButton1,urlButton1)
        time.sleep(1)
        
    # --- Button2 ---
    if GPIO.input(13) == GPIO.LOW:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print("Eingang 13 HIGH" )
        
        select_tab(tabButton2,urlButton2)
        time.sleep(1)
        time.sleep(1)
        
    # --- Button3 ---
    if GPIO.input(18) == GPIO.LOW:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print("Eingang 18 HIGH" )

        time.sleep(1)





