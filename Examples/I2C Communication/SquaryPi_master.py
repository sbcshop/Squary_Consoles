from machine import Pin, UART,SPI,I2C
import time,utime
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font

status = machine.Pin(25, machine.Pin.OUT)
status.value(0)

I2C_ADDR = [7,8,6] #I2C Address of SquaryFi's

i2c = I2C(1, sda=machine.Pin(2), scl=machine.Pin(3), freq=20000)
print("Initalizing I2C as Master")

data = "Hello Arduino" #Data to send to I2C device
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),
                    backlight=Pin(13, Pin.OUT),rotation=3)#SPI interface for tft screen

def display():
    tft.init()
    #wtime.sleep(0.5)#time delay
    tft.text(font,"SquaryPi Master", 0,20,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 55, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"Data Receive", 0,70,st7789.GREEN)
    tft.fill_rect(0, 105, 240,10, st7789.RED)

    tft.text(font,"From Address:", 0,120,st7789.YELLOW)
    tft.fill_rect(0, 160, 240,10, st7789.RED)
    
time.sleep(1)
display()
while 1:
    for i in range(len(I2C_ADDR)):
        status.value(1)
        rev = i2c.readfrom(I2C_ADDR[i],12) #readfrom(I2C_ADDR,number of bytes read)
        tft.text(font,rev.decode(), 10,180,st7789.WHITE)
        tft.text(font,str(I2C_ADDR[i]), 210,120,st7789.WHITE)
        print(rev.decode())
        utime.sleep(1)
