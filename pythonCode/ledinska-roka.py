'''
RasPi koda za krmiljenje roke direktno preko RaspberryPi
'''

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

# GPIO.setup(11,GPIO.OUT) # CHannel 11 je Output
# p = GPIO.PWM(11,50) # To pomeni, da na "kanalu" 11 startam PWM s frekvenoo 50 Herzov
# p.start(0) # Starta PWM z duty cyclom 0

# p.stop()
# GPIO.cleanup()

def Mozni_ukazi():
    p.ChangeFrequency(100) #Spremeni frekvenco na 100Hz

    p.ChangeDutyCycle(5) #Spremeni duty cycle (koliko casa bo High) kjerkoli med 0 pa 100 procenti
    print("Servoti sprejemajo samo impulze med 5 procenti duty cycla in 10 procenti")

def Initialize_Servo(x):
    control = []
    for pin in x:
        GPIO.setup(pin,GPIO.OUT)
        p = GPIO.PWM(pin,50)
        control.append(p);
    
    for p in control:
        p.start(5)
    print("Servo Initialized")
    return control

def Deinitialize_Servo(control):
    for servo in control:
        servo.stop()
    
    GPIO.cleanup()
    print("Servo deinitialized")

def kamen(control):
    for servo in control:
        servo.ChangeDutyCycle(10)
    print("kamen")

def skarje(control):
    for dolzina in range(len(control)):
        if (dolzina == 1) or (dolzina == 2):
            control[dolzina].ChangeDutyCycle(5)
        else:
            control[dolzina].ChangeDutyCycle(10)
    print("skarje")

def papir(control):
    for servo in control:
        servo.ChangeDutyCycle(5)
    print("Papir")

def testnakoda(control,spin):
    for servo in control:
        servo.ChangeDutyCycle(spin)
    print("Test complete")
        

def main():
    #Glede na "https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Header-with-Photo.png"
    servoPins = [32,33,12,35,31]; #GPIO 12 (pin 32),13 (pin 33),18 (pin 13),19(pin 35) imajo Hardwarski PWM, vsi majo pa lahk Softwarski PWM, jst sm kle dal GPIO6 (pin 31)
    control_PWM = Initialize_Servo(servoPins) #Pripravi vse servote in jih da na zacetno pozicijo
    #Moment of Truth
    control_PWM[1].ChangeDutyCycle(10)

    try:
        while (1):
            mode = input("kaj bi želel pokazati? :")
            if (mode.strip() == "kamen"):
                kamen(control_PWM)
                sleep(1)
            elif (mode.strip() == "papir"):
                papir(control_PWM)
                sleep(1)
            elif (mode.strip() == "skarje"):
                skarje(control_PWM)
                sleep(1)
            else:
                testnakoda(control_PWM,5)
                sleep(1)

    except KeyboardInterrupt:
        Deinitialize_Servo(control_PWM)

print("Hello World!")
print("Neki neki")
print("Megadeth")

main()