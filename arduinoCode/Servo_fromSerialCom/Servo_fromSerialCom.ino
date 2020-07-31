#include <Servo.h>

String PWMset = "50,50,50,50,50";
String kot;
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

void loop() { //koda ki pove servotom za koliko naj se obrnejo med 0 in 180
  
  kot = getValue(PWMset, ',', 0);
  palec.write(kot.toInt());
  kot = getValue(PWMset, ',', 1);
  kazalec.write(kot.toInt());
  kot = getValue(PWMset, ',', 2);
  sredinec.write(kot.toInt());
  kot = getValue(PWMset, ',', 3);
  prstanec.write(kot.toInt());
  kot = getValue(PWMset, ',', 4);
  mezinec.write(kot.toInt());
  delay(10);
}


void serialEvent() { /*Se ne izvede dokler loop ne pride do konca... prasec */
  PWMset = Serial.readString();
  Serial.println(PWMset);
}

String getValue(String data, char separator, int index)/* Parsa String v array, loči jih pa glede na separator char */
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
