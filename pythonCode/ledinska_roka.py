from time import sleep
import serial

def initializeServo():
    #NASTAVITVE ZA SERIJSKO KOMUNIKACIJO
    ser = serial.Serial(
            port='/dev/ttyS0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
    )
    return ser

def serial_communication(ser): # Modul za serijsko komunikacijo z Arduinom
    temp = str(input("kaj bi rad poslal?")) + "\r\n"
    vrvica = temp.encode() #User Input za podatke
    ser.write(vrvica)
    ser.flushOutput()
    sleep(1)
    ser.flushInput()
    b = ser.readline().decode('utf-8').rstrip() #In nato sprejmeš njegov odgovor
    print(b) #in ga javiš nazaj uporabniku
    sleep(1)

def sendDataToArduino_serial(data,ser):
    vrvica = data.encode() #User Input za podatke
    ser.write(vrvica)
    ser.flushOutput()
    sleep(1)
    ser.flushInput()
    b = ser.readline().decode('utf-8').rstrip() #In nato sprejmeš njegov odgovor
    print(b) #in ga javiš nazaj uporabniku
    sleep(1)
