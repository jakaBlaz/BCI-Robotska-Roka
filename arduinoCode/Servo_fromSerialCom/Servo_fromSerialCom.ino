#include <Servo.h>

String vrvica = "0";
int kot;
int servoPin3 = 3; 
int servoPin5 = 5; 
int servoPin6 = 6; 
int servoPin9 = 9; 
int servoPin10 = 10;
Servo palec;
Servo kazalec;
Servo sredinec;
Servo prstanec;
Servo mezinec;

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
  palec.attach(servoPin3);
  prstanec.attach(servoPin9);
  sredinec.attach(servoPin5);
  mezinec.attach(servoPin10); 
  kazalec.attach(servoPin6);
}

void loop() { //koda ki pove servotom za koliko naj se obrnejo med 0 in 255
  sredinec.write(kot);
  delay(2);
  palec.write(kot);
  delay(2);
  kazalec.write(kot);
  delay(2);
  prstanec.write(kot);
  delay(2);
  mezinec.write(kot);
  delay(2);
}

void serialEvent() { /*Se ne izvede dokler loop ne pride do konca*/
  Serial.flush(); //Pusha vse podatke (v in ven iz Arduinota)
  vrvica = Serial.readString(); //Prebere dobljene podatke kokr String
  kot = vrvica.toInt(); //spremenimo dobljeni podatek v tip integer
}
