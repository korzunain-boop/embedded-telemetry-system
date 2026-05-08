def parse_telemetry(decoded_line):
    data = {}

    measurments = decoded_line.split()

    for measurment in measurments:
        key, value = measurment.split("=")

        data[key] = int(value)

    return data