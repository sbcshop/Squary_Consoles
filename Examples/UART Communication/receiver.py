#SquaryPi Receiver code
import utime
from machine import Pin, UART,SPI
import time
import st7789

import vga1_8x16 as font1
import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=3)

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 0,20)
    tft.fill_rect(0, 60, 210,10, st7789.RED)
    
    tft.text(font,"SquaryPi", 0,75,st7789.YELLOW)
    tft.text(font,"Console", 0,150,st7789.YELLOW)
    tft.fill_rect(0, 130, 210, 10, st7789.BLUE)
    time.sleep(1)
    tft.fill(0) #clear screen
    tft.text(font,"RECEIVE DATA", 25,20,st7789.WHITE)
        
info()

while True:
    data_Read = uart.read(5)#read data comming from other pico lora expansion
    if data_Read is not None:
        print(data_Read)
        tft.text(font,data_Read, 80,80,st7789.YELLOW)
        utime.sleep(0.5)#wait 500ms
        tft.text(font,data_Read, 80,80,st7789.BLACK)
        tft.fill_rect(15, 60, 210,10, st7789.RED)
            
    
 


