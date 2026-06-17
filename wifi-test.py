import machine
from machine import SPI, Pin
import socket
import esp
import network
import time
import ubinascii
import utils
import os
from micropyserver import MicroPyServer
import wifi

wlan_id = "IMMLab24"
wlan_pass = "immlab24"

print(wifi.status())

sta, ap = wifi.reset(sta=True, ap=False,channel=6)
print(wifi.status())

wifi.connect(wlan_id, wlan_pass)

print(wifi.status())
