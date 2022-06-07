# Importing Libraries
import serial
import time
import base64
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("numara giriniz: ") # Taking input from user
    value = write_read(num)
    print(value)