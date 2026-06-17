import machine
from machine import SPI, Pin
import socket
from s28 import ILI9341
from s28.ILI9341 import LCD_28_ILI9341, SPI_W_SPEED, Delay_Ms
#from ST7796 import LCD_35_ST7796, SPI_W_SPEED, SPI_R_SPEED
from Font_12x24_EN import Font_12x24_EN
import esp
import time
#import ubinascii
import utils
import os
from micropyserver import MicroPyServer
import wifi

wlan_id = "IMMLab24"
wlan_pass = "immlab24"


#pin define
LCD_RS = 2
LCD_CS = 15
#LCD_RST = 27  #connect to ESP32 reset pin
LCD_SCK = 14
LCD_SDA = 13
LCD_SDO = 12
LCD_BL = 21

#color define
BLACK = 0x0000
WHITE = 0xFFFF
RED = 0xF800
GREEN = 0x07E0
BLUE = 0x001F
MAGENAT = 0xF81F
DARKBLUE = 0x01CF
LIGHTGREEN = 0x841F
spi = SPI(1,baudrate=SPI_W_SPEED,sck=Pin(LCD_SCK),mosi=Pin(LCD_SDA),miso=Pin(LCD_SDO))
#mylcd = LCD_35_ST7796(spi, LCD_CS, LCD_RS, LCD_BL)
mylcd = LCD_28_ILI9341(spi, LCD_CS, LCD_RS, LCD_BL)

wlan_id = "IMMLab24"
wlan_pass = "immlab24"

sta, ap = wifi.reset(sta=True, ap=False,channel=6)
print(wifi.status())
wifi.connect(wlan_id, wlan_pass)
print(wifi.status())


def Text_Width(text, font):
    x = 0
    chw = font['width']
    for i in text:
        x = x + chw
    return x

def show_text(text):
    w = Text_Width(text, Font_12x24_EN)
    x = int(mylcd.lcd_width/2) - int(w/2)
    mylcd.LCD_Clear(WHITE)
    mylcd.Show_String(x, int(mylcd.lcd_height/2)-16, text, Font_12x24_EN, BLACK)

def hello_world(request):
    ''' request handler '''
    server.send("HELLO WORLD!")

def show_params(request):
    global mylcd
    ''' request handler '''
    params = utils.get_request_query_params(request)
    print(params)
    if('t' in params):
        server.send("showing: {0}".format(params['t']))
        text = params['t']
        show_text(text)
    else:
        show_text("invalid request")
        server.send("invalid request")

server = MicroPyServer()
''' add route '''
server.add_route("/test", hello_world)
server.add_route("/", show_params)
''' start server '''
server.start()
       
