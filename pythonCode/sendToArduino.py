import sys
import glob
import serial

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    i = 0
    for x in result:
        print("{0}) {1}".format(i,x))
        i += 1
    port = input("izberi port (s številko)")

    return result[int(port)]

print("Please choose from one of available ports:")
port = serial_ports()
print (port)


ser = serial.Serial(port,9600)  # open serial port on COM7
while True:
    try:
        kot = (input("Vnesi cifro med 0-255: "))
        kot = kot.encode(encoding='ascii',errors='strict')

        ser.write(kot)
        ser.flush()
        preverjanje = ser.readline()
        print(preverjanje)
    except KeyboardInterrupt:
        ser.close()
        exit()