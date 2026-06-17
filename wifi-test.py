import machine
from machine import SPI, Pin
import socket
from ST7796 import LCD_35_ST7796, SPI_W_SPEED, SPI_R_SPEED
from Font_8x16_EN import Font_8x16_EN
import esp
import network
import time
import ubinascii
import utils
import os
from micropyserver import MicroPyServer

wlan_id = "wifiSSID"
wlan_pass = "wifipass"

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print("MAC: " + mac)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while wlan.status() is network.STAT_CONNECTING:
    time.sleep(1)
while not wlan.isconnected():
    wlan.connect(wlan_id, wlan_pass)
print("Connected... IP: " + wlan.ifconfig()[0])  


#pin define
LCD_RS = 2
LCD_CS = 15
#LCD_RST = 27  #connect to ESP32 reset pin
LCD_SCK = 14
LCD_SDA = 13
LCD_SDO = 12
LCD_BL = 27

#color define
BLACK = 0x0000
WHITE = 0xFFFF
RED = 0xF800
GREEN = 0x07E0
BLUE = 0x001F
MAGENAT = 0xF81F
DARKBLUE = 0x01CF
LIGHTGREEN = 0x841F

color_list = [RED, MAGENAT, GREEN, DARKBLUE, BLUE, BLACK, LIGHTGREEN]

spi = SPI(1,baudrate=SPI_W_SPEED,sck=Pin(LCD_SCK),mosi=Pin(LCD_SDA),miso=Pin(LCD_SDO))
mylcd = LCD_35_ST7796(spi, LCD_CS, LCD_RS, LCD_BL)

addr = wlan.ifconfig()[0]


mylcd.LCD_Clear(WHITE)
mylcd.Show_String(10, 30, addr, Font_8x16_EN, BLACK)

def hello_world(request):
    ''' request handler '''
    server.send("HELLO WORLD!")

def show_params(request):
    global mylcd
    ''' request handler '''
    params = utils.get_request_query_params(request)
    print(params)
    server.send("showing: {0}".format(params['t']))
    text = params['t']
    mylcd.LCD_Clear(WHITE)
    mylcd.Show_String(10,30,text,Font_8x16_EN, BLACK)


server = MicroPyServer()
''' add route '''
server.add_route("/test", hello_world)
server.add_route("/", show_params)
''' start server '''
server.start()
       
