import serial
import time

ser = serial.Serial("COM9", 115200)

while 1:
    ser.write(b'0')
    time.sleep(0.500)
    ser.write(b'1')
    time.sleep(0.500)