
# AquaTrioPico - System podlewania 3 roślin z wyświetlaczem OLED
# Wersja MicroPython na PicoPi (Raspberry Pi Pico)

from machine import Pin, ADC, I2C
from time import sleep
import ssd1306

# Ustawienia pinów
relay_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]
moisture_pins = [ADC(26), ADC(27), ADC(28)]

# I2C i OLED (128x64)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Progi wilgotności (wartości ADC)
thresholds = [30000, 30000, 30000]  # dostosuj do swoich czujników

def read_moisture(index):
    value = moisture_pins[index].read_u16()
    return value

def water_plant(index, duration=3):
    oled.fill(0)
    oled.text(f"Podlewam: Roślina {index+1}", 0, 0)
    oled.show()
    relay_pins[index].value(1)
    sleep(duration)
    relay_pins[index].value(0)

def update_oled(status):
    oled.fill(0)
    for i, val in enumerate(status):
        oled.text(f"R{i+1}: {val}", 0, i*10)
    oled.show()

while True:
    status = []
    for i in range(3):
        moisture = read_moisture(i)
        status.append(moisture)
        if moisture < thresholds[i]:
            water_plant(i)
    update_oled(status)
    sleep(10)
