import serial

SERIAL_PORT = "COM3"
BAUDRATE = 115200

def read_serial():
    ser = serial.Serial(
        port = SERIAL_PORT,
        baudrate = BAUDRATE,
        timeout=1
    )

    print(f"Connected to {SERIAL_PORT}")

    while True:
        line = ser.readline()

        if line:
            decoded = line.decode("utf-8").strip()

            print(decoded)

if __name__ == "_main_":
    read_serial()























import serial

SERIAL_PORT = "COM5"
BAUDRATE = 115200

def read_serial():
    ser = serial.Seriall(
        port = SERIAL_PORT,
        baudrate = BAUDRATE,
        timeout = 1
    )

    while True:
        line = ser.readline()

        if line:
            decode = line.decode("utf-8").strip()

            print(line)


if __name__ == "__main__":
    read_serial()