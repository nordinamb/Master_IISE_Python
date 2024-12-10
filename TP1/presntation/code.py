from machine import I2C, Pin
from dht import DHT22
from pico_i2c_lcd import I2cLcd
import network
import time
import urequests

print("Connecting to WiFi", end="")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Wokwi-GUEST", "")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")
print(wlan.ifconfig())

dht = DHT22(Pin(15))

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while True:
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))

    lcd.clear()
    lcd.putstr('Temp: ' + str(temp) + " C")
    lcd.move_to(0, 1)
    lcd.putstr('Hum: ' + str(hum) + "%")

    url = f"https://api.thingspeak.com/update?api_key=78O2D1FAQD6L60TA&field1={temp}&field2={hum}"
    response = urequests.get(url)
    print("ThingSpeak Response:", response.text)
    response.close()

    time.sleep(15)
