import serial #knjižnica PySerial
ser = serial.Serial('COM7',9600)  # open serial port

while True:
    try:
        kot = (input("Vnesi cifro med 0-255:"))
        kot = kot.encode(encoding='ascii',errors='strict')

        ser.write(kot)
        ser.flush()
    except KeyboardInterrupt:
        ser.close()
        exit()