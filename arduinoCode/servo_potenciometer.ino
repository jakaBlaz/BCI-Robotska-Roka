#include <Servo.h> 
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
 palec.attach(servoPin3);
 prstanec.attach(servoPin9);
 sredinec.attach(servoPin5);
 mezinec.attach(servoPin10); 
 kazalec.attach(servoPin6);
}
void loop() {
 int val = analogRead(0);
  val = map(val, 0, 1023, 0, 180);
sredinec.write(val);
delay(2);
palec.write(val);
delay(2);
kazalec.write(val);
delay(2);
prstanec.write(val);
delay(2);
mezinec.write(val);
delay(2);
}

// to je komentar
