import serial
import time

ser = serial.Serial("COM9", 115200)
ser.reset_input_buffer

while True:
    command = input("Command: ")

    ser.write((command + "\n").encode())
    response = ser.readline().decode().strip()

    print("STM32: " + response)
