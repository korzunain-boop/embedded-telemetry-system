import serial

SERIAL_PORT = "COM3"
BAUDRATE = 115200


def read_serial():
    ser = serial.Serial(
        port=SERIAL_PORT,
        baudrate=BAUDRATE,
        timeout=1
    )

    while True:
        line = ser.readline()

        if line:
            decoded = line.decode("utf-8").strip()

            yield decoded