import machine
from machine import SPI, Pin
import socket
from s28 import ILI9341
from s28.ILI9341 import LCD_28_ILI9341, SPI_W_SPEED, Delay_Ms
#from ST7796 import LCD_35_ST7796, SPI_W_SPEED, SPI_R_SPEED
from Font_16x32_EN import Font_16x32_EN
#from Font_12x24_EN import Font_12x24_EN
import esp
import network
import time
#import ubinascii
import utils
import os
from micropyserver import MicroPyServer

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

color_list = [RED, MAGENAT, GREEN, DARKBLUE, BLUE, BLACK, LIGHTGREEN]

spi = SPI(1,baudrate=SPI_W_SPEED,sck=Pin(LCD_SCK),mosi=Pin(LCD_SDA),miso=Pin(LCD_SDO))
#mylcd = LCD_35_ST7796(spi, LCD_CS, LCD_RS, LCD_BL)
mylcd = LCD_28_ILI9341(spi, LCD_CS, LCD_RS, LCD_BL)


mylcd.LCD_Clear(WHITE)

def Text_Width(text, font):
    x = 0
    chw = font['width']
    for i in text:
        x = x + chw
    return x

def show_text(text):
    w = Text_Width(text, Font_16x32_EN)
    x = int(mylcd.lcd_width/2) - int(w/2)
    mylcd.LCD_Clear(WHITE)
    mylcd.Show_String(x, int(mylcd.lcd_height/2)-16, text, Font_16x32_EN, BLACK)

    

show_text("hello, world")

