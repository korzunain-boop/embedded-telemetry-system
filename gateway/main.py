from serial_reading import read_serial
from parser import parse_telemetry

def main():
    for line in read_serial():
        parsed = parse_telemetry(line)

        print(parsed)

if __name__ == "__main__":
    main()