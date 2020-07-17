import bisijao as bci
import plot
import sendToArduino as roka

#Acquire data
signal,signal_fft = plot.plotFromTxt(200,1.0,50.0,35.0)

#send data
serial = roka.initializeServo()
vrnjeno, uspesno = roka.sendData("125",serial)
print(vrnjeno)
print(uspesno)
serial.close()