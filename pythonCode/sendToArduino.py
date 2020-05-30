import serial #knjižnica PySerial
ser = serial.Serial('COM5',9600)  # open serial port
ser.write(b'125')
ser.flush()